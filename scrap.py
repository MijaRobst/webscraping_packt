from bs4 import BeautifulSoup
import urllib2


URL = "https://www.packtpub.com/packt/offers/free-learning/"


def print_info(title, subtitle, description):
    """
    Print the given elements.

    The format is:
        <title>
            <subtitle>
            * <description[0]>
            * <description[1]>
            ...
    """
    print("******** Info from " + URL + " ********")

    print("\n" + title + "\n")
    print("\t" + subtitle + "\n")
    for item in description:
        print("\t* " + str(item.text.strip().encode('ascii', 'ignore')) + "\n")


def scrap():
    """
    Access PACKT free learning book webpage and display its info.

    Gets the book's title, subtitle and general information, printing it.
    """
    html = urllib2.urlopen(URL).read()
    soup = BeautifulSoup(html, "lxml")

    # Get title
    title = soup.find("h2")

    # Get subtitle (by navigating from title)
    subtitle = title.parent.parent.find_all("div")[2].text

    # Get bullet points
    bullet_points = soup.find_all("li")

    print_info(title.text.strip(), subtitle.strip(), bullet_points)


if __name__ == "__main__":
    scrap()
