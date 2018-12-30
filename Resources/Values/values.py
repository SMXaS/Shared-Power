############################
# Colors
############################
bgColor = "#0D47A1"
fgColor = "white"
errorColor = "#FA8072"
bgInactive = "grey"


############################
# Strings
############################
appTitle = "Shared Power"
asterix = "*"
currency = "$"
back = "Back"
dateFormat = "%d/%m/%Y"
welcomeText = "Welcome to Shared Power!!!"
# --------------
# Image Paths
# --------------
buttonAdd = "Resources/Drawable/btn_add.png"
buttonBack = "Resources/Drawable/btn_back.png"
buttonHire = "Resources/Drawable/btn_hire.png"

# --------------
# Database
# --------------
fieldNames_user = ['login', 'first_name', 'last_name', 'user_password', 'email', 'user_adress', 'user_phone_number']
fieldNames_tool = ['ID', 'owner', 'title', 'description', 'condition', 'priceFullDay', 'priceHalfDay', 'imgPath',
                   'availability']
fieldNames_booking = ['toolID', 'userName', 'bookInCondition', 'startDate', 'startTerm', 'expectedReturnDate',
                      'expectedTerm', 'returnDate', 'bookOutCondition', 'pickUpLocation', 'dropOffLocation']
filePath_user = "Data/users.csv"
filePath_tool = "Data/tools.csv"
filePath_booking = "Data/Bookings/"
filePath_invoiceFolder = "Data/Invoices/{}"
filePath_images = "Data/Images/"

# --------------
# Main Menu
# --------------
menuMyTools = "My Tools"
menuMyBookings = "My Bookings"
menuAddTool = "Add Tool"
menuSearchTool = "Search Tool"
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
addToolTitle = "Add tool"
toolTitle = "Title "
toolDescription = "Description "
priceDay = "Price per Day "
priceHalfDay = "Price per Half Day "
toolCondition = "Tool condition "
emptyIMGPath = "..."
image = "Image"

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

# --------------
# My Tools Page
# --------------
myToolTitle = "My Tools"

# --------------
# Return Tool Page
# --------------
tool = "Tool"

# --------------
# Search Tool Page
# --------------
searchToolTitle = "Search..."
search = "Search"

# --------------
# Login Page
# --------------
loginTitle = "Login"
dontHaveAccount = "Don't have Account?"
signUp = "Sign up"

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

############################
# Dimens
############################
registerWindowWidth = 280
registerWindowHeigh = 340
mainWindowWidth = 800
mainWindowHeigh = 500


############################
# Fonts
############################
addImageFont = "Helvetica 10 underline bold"
dontHaveAccountFont = "Helvetica 7 italic"
signUpFont = "Helvetica 7 bold underline"
buttonFont = "Helvetica 10 bold"
welcomeFont = "Helvetica 16"
