from bs4 import BeautifulSoup
import urllib2


def print_info(title, subtitle, description):
    print("\n" + title + "\n")
    print("\t" + subtitle + "\n")
    for item in description:
        print("\t* " + str(item.text.strip().encode('ascii', 'ignore')) + "\n")


if __name__ == "__main__":
    html = urllib2.urlopen("https://www.packtpub.com/packt/offers/"
                           + "free-learning/").read()
    soup = BeautifulSoup(html, "lxml")

    # Get title
    title = soup.find("h2")

    # Get subtitle
    subtitle = title.parent.parent.find_all("div")[2].text

    # Get bullet points
    bullet_points = soup.find_all("li")

    print_info(title.text.strip(), subtitle.strip(), bullet_points)
