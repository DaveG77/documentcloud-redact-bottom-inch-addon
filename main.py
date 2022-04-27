"""
This is a hello world add-on for DocumentCloud.

It demonstrates how to write a add-on which can be activated from the
DocumentCloud add-on system and run using Github Actions.  It receives data
from DocumentCloud via the request dispatch and writes data back to
DocumentCloud using the standard API
"""
from listcrunch import uncrunch
from documentcloud.addon import AddOn

class RedactInch(AddOn):
    def main(self):

        if not self.documents:
            self.set_message("Please select at least one document")

        self.set_message("Redact Bottom Inch start!")

        for document in self.client.documents.list(id__in=self.documents):
            #go through each page
            pages = document.page_count

            #to hold the redacttion json dictionary for each individual page in this document
            eachPage = []

            for page in range(pages):
                #append the specific json dict for this page to global dict
                eachPage.append({"page_number": page, "x1": 0, "y1": 0.9, "x2": 1, "y2": 1})

            #make the api call for this document
            self.client.post(f"documents/{document.id}/redactions/", json=eachPage)

        self.set_message("Redact Bottom Inch end!")
if __name__ == "__main__":
    RedactInch().main()
