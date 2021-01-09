from requests_html import HTML, HTMLSession

session = HTMLSession()

#Rtx 3060 ti that are located at verkkokauppa
shops = {'verkkokauppa': ['https://www.verkkokauppa.com/fi/product/10047/qggrm/MSI-GeForce-RTX-3060-Ti-VENTUS-2X-OCV1-naytonohjain-PCI-e-va?list=OZCYkRqSdAzqHQzcqH2z8qHQU9qH2hDqjFMsqjXDtqjXoEqHQkvqH2Xyi',
                          'https://www.verkkokauppa.com/fi/product/6818/qfbsf/Asus-ROG-STRIX-RTX3060TI-O8G-GAMING-naytonohjain-PCI-e-vayla?list=OZCYkRqSdAzqHQzcqH2z8qHQU9qH2hDqjFMsqjXDtqjXoEqHQkvqH2Xyi',
                          'https://www.verkkokauppa.com/fi/product/43967/qfbtd/Asus-DUAL-RTX3060TI-8G-naytonohjain-PCI-e-vaylaan?list=OZCYkRqSdAzqHQzcqH2z8qHQU9qH2hDqjFMsqjXDtqjXoEqHQkvqH2Xyi',
                          'https://www.verkkokauppa.com/fi/product/19435/qfbsn/Asus-TUF-RTX3060TI-O8G-GAMING-naytonohjain-PCI-e-vaylaan?list=OZCYkRqSdAzqHQzcqH2z8qHQU9qH2hDqjFMsqjXDtqjXoEqHQkvqH2Xyi',
                          'https://www.verkkokauppa.com/fi/product/65299/qfbss/Asus-TUF-RTX3060TI-8G-GAMING-naytonohjain-PCI-e-vaylaan?list=OZCYkRqSdAzqHQzcqH2z8qHQU9qH2hDqjFMsqjXDtqjXoEqHQkvqH2Xyi',
                          'https://www.verkkokauppa.com/fi/product/47656/qfxfn/MSI-GeForce-RTX-3060-Ti-VENTUS-2X-OC-naytonohjain-PCI-e-vayl?list=OZCYkRqSdAzqHQzcqH2z8qHQU9qH2hDqjFMsqjXDtqjXoEqHQkvqH2Xyi',
                          'https://www.verkkokauppa.com/fi/product/39983/qfxfb/MSI-GeForce-RTX-3060-Ti-GAMING-X-TRIO-naytonohjain-PCI-e-vay?list=OZCYkRqSdAzqHQzcqH2z8qHQU9qH2hDqjFMsqjXDtqjXoEqHQkvqH2Xyi',
                          'https://www.verkkokauppa.com/fi/product/33008/qfxfj/MSI-GeForce-RTX-3060-Ti-VENTUS-3X-OC-naytonohjain-PCI-e-vayl?list=OZCYkRqSdAzqHQzcqH2z8qHQU9qH2hDqjFMsqjXDtqjXoEqHQkvqH2Xyi',
                          'https://www.verkkokauppa.com/fi/product/21952/qfbsj/Asus-ROG-STRIX-RTX3060TI-8G-GAMING-naytonohjain-PCI-e-vaylaa?list=OZCYkRqSdAzqHQzcqH2z8qHQU9qH2hDqjFMsqjXDtqjXoEqHQkvqH2Xyi',
                          'https://www.verkkokauppa.com/fi/product/36773/qfbsx/Asus-DUAL-RTX3060TI-O8G-naytonohjain-PCI-e-vaylaan?list=OZCYkRqSdAzqHQzcqH2z8qHQU9qH2hDqjFMsqjXDtqjXoEqHQkvqH2Xyi']}
        
#Function to get availability of rtx 3060 ti cards at verkkokauppa.com
def verkkokauppaAvailability():

    #Loops through all the gpus
    counter = -1
    for gpu in shops['verkkokauppa']:
        counter += 1
        #Gets the html of store site
        resp = session.get(shops['verkkokauppa'][counter])
        resp.html.render()
        resp.html.html

        #Finding the html corresponding to availability
        article = resp.html.find('.lt2tbg-0', first=True)
        availability = article.find('.shipment-details', first=True).text

        #Check if the card is available
        if "ei vahvistettu" or "Ei saatavilla" in availability:
            print(shops['verkkokauppa'][counter] + "\n" + "Lähetettävissä: ei vahvistettu")
        else:
            print("Lähetettävissä! " + shops['verkkokauppa'][counter])


verkkokauppaAvailability()
