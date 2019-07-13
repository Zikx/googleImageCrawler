from icrawler.builtin import GoogleImageCrawler
# import argparse

print("\nGoogle Image Crawler\n---------------------------------\nVer1 By Zikx\n---------------------------------\n")
word = input("Search : ")
dir_name = input("dir name :")
# parser = argparse.ArgumentParser()
# parser.add_argument("-search", "--searchImages",nargs='*', required=True)

# args = parser.parse_args()

# searchImages = args.searchImages
def main():
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=1,
        downloader_threads=4,
        storage={'root_dir': dir_name})

    google_crawler.crawl(keyword=word, offset=0, max_num=1000,
                        min_size=(200,200), max_size=None, file_idx_offset=0)


if __name__=="__main__":
    main()