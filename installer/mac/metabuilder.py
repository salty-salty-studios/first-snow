from datetime import datetime, timezone
import ds_store
import biplist
import mac_alias

BACKGROUND_PATH = '.background.png'

def create_alias(volname, filename):
    volume = mac_alias.VolumeInfo(
        volname, datetime.now(timezone.utc),
        fs_type=mac_alias.ALIAS_HFS_VOLUME_SIGNATURE, disk_type=mac_alias.ALIAS_FIXED_DISK,
        attribute_flags=0, fs_id=bytes(2),
    )
    target = mac_alias.TargetInfo(
        mac_alias.ALIAS_KIND_FILE, filename,
        folder_cnid=0, cnid=0, creation_date=datetime.now(timezone.utc),
        creator_code=bytes(4), type_code=bytes(4),
        folder_name=volname, carbon_path='{}:{}'.format(volname, filename),
    )
    return mac_alias.Alias(volume=volume, target=target)

class DMGMetadata:
    def __init__(self, name, outfile):
        self.name = name
        self.store = ds_store.DSStore.open(outfile, 'w+')
        self.store['.']['vSrn'] = ('long', 1)
        self.store['.']['icvl'] = ('type', 'icnv')
        self.store['.']['icvp'] = {
            'viewOptionsVersion': 1,

            'gridSpacing': 100.0,
            'gridOffsetX': 0.0,
            'gridOffsetY': 0.0,
            'scrollPositionY': 0.0,

            'labelOnBottom': True,
            'showItemInfo': False,
            'showIconPreview': False,
            'iconSize': 88.0,
            'textSize': 14.0,

            'backgroundType': 2,
            'backgroundColorRed': 1.0,
            'backgroundColorBlue': 1.0,
            'backgroundColorGreen': 1.0,

            'arrangeBy': 'none',
        }
        self.store['.']['bwsp'] = {
            'ShowTabView': False,
            'ShowStatusBar': False,
            'ShowToolbar': False,
            'ShowPathbar': False,
            'ShowSidebar': False,
            'ContainerShowSidebar': False,
            'PreviewPaneVisibility': False,
            'SidebarWidth': 180,
        }

    def set_background_size(self, x, y):
        d = self.store['.']['icvp']
        d.update({
            'backgroundImageAlias': biplist.Data(create_alias(self.name, BACKGROUND_PATH).to_bytes())
        })
        self.store['.']['icvp'] = d

        d = self.store['.']['bwsp']
        d.update({
            'WindowBounds': '{{100, 100}, {%s, %s}}' % (x, y)
        })
        self.store['.']['bwsp'] = d

    def add_icon(self, filename, x, y):
        self.store[filename]['Iloc'] = (x, y)

    def close(self):
        self.store.close()

    
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--background-size', type=lambda v: v.split(':'))
    parser.add_argument('-i', '--icon-pos', type=lambda v: v.split(':'), action='append', default=[])
    parser.add_argument('-n', '--name')
    parser.add_argument('outfile')

    args = parser.parse_args()

    metadata = DMGMetadata(args.name, args.outfile)
    if args.background_size:
        x, y = args.background_size
        metadata.set_background_size(int(x), int(y))
    for (file, x, y) in args.icon_pos:
        metadata.add_icon(file, int(x), int(y))

    metadata.close()
