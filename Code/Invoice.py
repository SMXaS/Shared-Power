import Code.Utilities.WriteFile as wf

class Invoice:

    def __init__(self, booking, user):
        """
        :param booking: object
        :param user
        """

        self.booking = booking
        self.user = user

    def generateInvoice(self):
        wf.add_invoice()

    def showInvoice(self):
        pass
