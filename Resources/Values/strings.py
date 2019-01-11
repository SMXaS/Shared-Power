appTitle = "Shared Power"
asterisk = "*"
currency = "£"
back = "Back"
dateFormat = "%#d/%#m/%Y"
simpleDateFormat = "%d/%m/%Y"
invoiceMonth_YearFormat = "%#m-%Y"
invoiceYearFormat = "%Y"
invoiceMonthFormat = "%#m"
welcomeText = "Welcome to Shared Power!!!"
# --------------
# Classes
# --------------
myProfileClass = "MyProfilePage"
myToolClass = "MyToolPage"
addToolClass = "AddToolPage"
bookToolClass = "BookToolPage"
loginClass = "LoginPage"
registerClass = "RegisterPage"
returnToolClass = "ReturnToolPage"
searchToolClass = "SearchToolPage"
welcomeClass = "WelcomePage"
invoiceClass = "InvoicePage"
toolInfoPage = "ToolInfoPage"
receiveToolPage = "ReceiveToolPage"
emptyLayout = "EmptyLayout"

# --------------
# Image Paths
# --------------
btn_add = "Resources/Drawable/btn_add.png"
buttonEditTool = "Resources/Drawable/btn_edit.png"
btn_confirm = "Resources/Drawable/btn_confirm.png"
btn_delete = "Resources/Drawable/btn_delete.png"
btn_return = "Resources/Drawable/btn_return.png"
btn_cancel = "Resources/Drawable/btn_cancel.png"
btn_change_availability = "Resources/Drawable/btn_change_availability.png"
btn_back = "Resources/Drawable/btn_back.png"
buttonHire = "Resources/Drawable/btn_hire.png"
account = "Resources/Drawable/account.png"
search_img = "Resources/Drawable/search.png"
tool_img = "Resources/Drawable/menu.png"
bookings_img = "Resources/Drawable/bookings_img.png"
invoice_img = "Resources/Drawable/invoice_img.png"
add_img = "Resources/Drawable/add_img.png"

# --------------
# Dialogs
# --------------
infoDialogTitle = "Info"
confirmDialogTitle = "Confirmation"
cancelDialogMessage = "Your booking has been canceled"
returnDialogMessage = "Item has been returned"

# --------------
# Tool
# --------------
toolStatus = ["hired", "pending_receive", "inventory"]

# --------------
# Database
# --------------
fieldNames_user = ['login', 'first_name', 'last_name', 'user_password', 'email', 'user_adress', 'user_phone_number']
fieldNames_tool = ['ID', 'owner', 'title', 'description', 'condition', 'priceFullDay', 'priceHalfDay', 'riderCharge',
                   'imgPath', 'availability']
fieldNames_booking = ['bookingID', 'toolID', 'userName', 'bookInCondition', 'startDate', 'startTerm',
                      'expectedReturnDate', 'expectedTerm', 'status', 'returnDate', 'bookOutCondition',
                      'pickUpLocation', 'dropOffLocation']
fieldNames_invoice = ['user', 'toolTitle', 'hirePrice', 'riderPrice', 'fine']
filePath_user = "Data/users.csv"
filePath_tool = "Data/tools.csv"
filePath_booking = "Data/Bookings/"
filePath_allBookings = "Data\Bookings\*.csv"
filePath_invoiceFolder = "Data/Invoices/"
filePath_images = "Data/Images/"

# --------------
# Main Menu
# --------------
menuMyTools = "My Tools"
menuMyBookings = "My Bookings"
menuAddTool = "Add Tool"
menuSearchTool = "Search Tool"
menuInvoice = "Invoices"
menuLogOut = "Log Out"
myProfile = "My Profile"
# --------------
# Register Page
# --------------
registerTitle = "Register"
firstName = "First name"
lastName = "Last name"
userName = "User name"
postCode = "Post code"
streetName = "Street name"
houseNumber = "House number"
email = "Email"
emailConfirmation = "Email confirmation"
password = "Password"
passwordConfirmation = "Password confirmation"
phoneNumber = "Phone number"
createAccount = "Create account"

# --------------
# Add Tool Page
# --------------
addToolTitle = "Add Tool"
editToolTitle = "Edit Tool"
toolTitle = "Title "
toolDescription = "Description "
priceDay = "Price per Day "
priceHalfDay = "Price per Half Day "
toolCondition = "Tool condition "
emptyIMGPath = "..."
image = "Image"
dispatchCharge = "Rider's cost "

# --------------
# Book Tool Page
# --------------
bookToolTitle = "Hire Tool"
owner = "Owner "
hireDate = "Hire date"
returnDate = "Return date"
fullDay = "Full day"
halfDay = "Half day"
arrangeRider = "Arrange rider"
pickUpLocation = "Pick up location "
dropOffLocation = "Drop off location "
confirmBooking = "Do you want to hire this tool?"

# --------------
# My Tools Page
# --------------
myToolTitle = "My Tools"
availability = "Availability"
fullDayPrice = "Full day price"
halfDayPrice = "Half day price"
changeAvailabilityConfirm = "Do you really want to change availability of this item?"

# --------------
# My Bookings Page
# --------------
cancelItemConfirm = "Do you really want to cancel this booking?"

# --------------
# Return Tool Page
# --------------
tool = "Tool"
returnItem = "Return item"
cancelBooking = "Cancel booking"
cancelErrorMessage = "Sorry, its too late to cancel"
bookOutConditionLabel = "*Please provide tool condition"

# --------------
# Tool Info Page
# --------------
showImage = "Show image"

# --------------
# Search Tool Page
# --------------
searchToolTitle = "Search..."
btn_search = "Search"
toolInfo = "Tool information"

# --------------
# Login Page
# --------------
loginTitle = "Login"
dontHaveAccount = "Don't have Account?"
signUp = "Sign up"

# --------------
# Invoice Page
# --------------
totalCost = "Total cost: "
toolTitleForInvoice = "Tool title:"
toolCost = "Tool cost:"
dispatchCost = "Dispatch cost:"
fines = "Fines:"
flatCharge = "Flat charge:"

# --------------
# Receive Item Page
# --------------
receiveItem = "Receive items"
declareAsDamaged = "Declare as damaged"

# --------------
# Error messages
# --------------
errorSomethingWrong = "Something went wrong"
errorUserDoesntExist = "User does not exist"
errorUserAlreadyExist = "User already exist"
errorIncorrectPassword = "Incorrect password"
errorEmptyFields = "Some fields are empty"
errorSpaces = "some fields contain spaces"
errorEmailMismatch = "Email does not match"
errorInvalidEmail = "Invalid email address"
errorPasswordMismatch = "Password does not match"
errorShortPassword = "Password is too short"
errorInvalidPhoneNumber = "Invalid phone number"
errorWrongImageFormat = "Wrong image format"
errorUnsupportedImageFormat = "Only .png format supported"
errorIncorrectPriceFormat = "Incorrect Price format"
errorSelectItem = "Please select item first"
errorToolConditionMissing = "Please describe the tool condition"
errorAlreadyBooked = "Sorry, but this item has been booked already.."
errorEmptyList = "Your list is empty"
