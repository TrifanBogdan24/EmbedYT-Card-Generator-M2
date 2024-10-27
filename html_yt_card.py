#!/usr/bin/env python3


from pytubefix import YouTube
import sys


def print_html_code_for_youtube_card(URL: str, VIDEO_ID: str, TITLE: str, DURATION: str) -> None:
    """
    DURATION = total duration of the videoclip, in seconds
    DO NOT format the DURATION!
    """
    print(f"<!-- {TITLE} -->")
    print(f"<a href=\"{URL}\">")
    print(f"<picture>")
    print(f"\t<source media=\"(prefers-color-scheme: dark)\" srcset=\"https://ytcards.demolab.com/?id={VIDEO_ID}&title={TITLE.replace(' ', '+')}&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&max_title_lines=2&width=250&border_radius=5&duration={DURATION}\">")
    print(f"\t<img src=\"https://ytcards.demolab.com/?id={VIDEO_ID}&title={TITLE.replace(' ', '+')}&background_color=%23ffffff&title_color=%2324292f&stats_color=%2357606a&max_title_lines=2&width=250&border_radius=5&duration={DURATION}\" alt=\"{TITLE}\" title=\"{TITLE}\">")
    print("</picture>")
    print("</a>")



def autoget_youtube_video_info(URL: str) -> tuple[str, str, str]:
    """
    If the online resources are located, the function will return a tuple, containing:
    - The URL of the Thumbnail
    - The Title of the YouTube clip
    - The Duration of the YouTube clip
    """
    try:
        # Create a YouTube object
        yt = YouTube(URL, use_oauth=True, allow_oauth_cache=True)

        # Get YouTube clip info
        video_id: str = yt.video_id
        title: str = yt.title
        duration: int = yt.length  # Duration in seconds


        return (video_id, title, duration)
    except Exception as e:
        print(f"[ERROR] Something went wrong while retrieving YouTube information!", file=sys.stderr)
        print(f"[ERROR] {e}", file=sys.stderr)
        print(f"Please make sure the provided URL is from YouTube, the URL works and you have internet connection.")
        sys.exit(1)



def help_option() -> None:
    print("NAME:")
    print(f"\t{sys.argv[0]} - generates HTML / MarkDown code for a YouTube clickable card.")
    print()
    print(f"DESCRIPTION:")
    print(f"\t{sys.argv[0]} requires a single argument, the URL of the YouTube clip.")
    print(f"\tThe script will automatically fetch, from online, metadata (info) of the YouTube Video/Short,")
    print(f"\tincluding THUMBNAIL PICTURE's URL, TITLE, DURATION.")
    print()
    print(f"\tWithout internet connection, the script doesn't work.")
    print(f"\tIt will generate an error message.")
    print()
    print(f"\tThe generated HTML/MarkDown code will include a thumbnail, containing a white arrow in a red circle.")
    print(f"\tThe text of the URL will be rendered above the title, both being splitted by a line, and aligned to the left.")
    print(f"\tThe code will also include relevant comments.")
    print()
    print("USAGE:")
    print(f"\t$ {sys.argv[0]} $URL")
    print(f"\t$ {sys.argv[0]} --url=$URL")
    print()
    print(f"\t$ {sys.argv[0]} -h")
    print(f"\t$ {sys.argv[0]} --help")
    print()
    print("OPTIONS:")
    print("\t-h, --help     Display this suggestive help text and exit.")
    print(f"\t--url=        Pass the URL as value to this flag.")
    print()
    print("See more info at project home page: https://github.com/TrifanBogdan24/EmbedYT-Card-Generator-M2.git")
    print()


def main():
    if len(sys.argv) != 2:
        print(f"[ERROR] Invalid number of arguments!", file=sys.stderr)
        print(f"[ERROR] The script expects a single argument!", file=sys.stderr)
        print(f"Please run '{sys.argv[0]} --help' to see the available options.", file=sys.stderr)
    else:
        if sys.argv[1] in ['-h', '--help']:
            help_option()
        else:
            URL = ''
            if sys.argv[1].startswith('--url='):
                URL = sys.argv[1].removeprefix('--url=')
            else:
                URL = sys.argv[1]
            
            (VIDEO_ID, TITLE, DURATION) = autoget_youtube_video_info(URL)
            print_html_code_for_youtube_card(
                URL, VIDEO_ID, TITLE, DURATION
            )


if __name__ == '__main__':
    main()

