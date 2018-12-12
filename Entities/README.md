## User:
  
**it takes:**

    user name (str)
    first name (str)
    last name (str)
    password (str)
    post code (str)
    email (str)
    address (str)
    phone (str)
   
**usage:**
    
   *initialize*
   
    from Entities.User import User
    user1 = User(arg, arg2, ...)
    
   *getting data*
   
    user1.getName()
    user1.getLastName()
    ...

## Tool:

**it takes:**
    
    ID (str)
    owner (user login) (str)
    title (str)
    description (str)
    full day price (float)
    half day price (float)
    image path (str)
    availability (boolean)
    
**usage**

*initialize*

    from Entities.Tool import Tool
    myTool = Tool(arg, arg2, ...)
    
 *usage*
 
    myTool.getID()
    myTool.getOwner()
    myTool.isAvailable()
    ...
    
 *change availability*
    
    --preCondition--
    you must have that object already
    ---------------------------------
    myTool.setAvailability(True/False)
