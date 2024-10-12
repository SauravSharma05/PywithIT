# a = 10
# b = 'hi'
# print(f'we can print both variables as {a} and {b}')

# str and repr are two debugging tools for converting to any string 
# text1 = 'hello, motto'
# debug_text = str(text1)
# print(debug_text)

# text2 = 'hello, motto'
# debug_text = repr(text2)
# print(debug_text)


# !a : ascii
# !s : str()
# !r : repr()

# formatting text
# print('this is {} and {}'.format('a', 'b'))
# print('this is {0} and {1}'.format('a', 'b'))   // for position

# def local_class_ex:
# def local_func:
# text1 = 'local hello'

# def non_local_func:
# text1 = 'non local hello'

# def global_func:
# text1 = 'non local hello'

# text1 = "normal hello"

# local_func()
# print('local function output : ', text1)


# non_local_func()
# nonlocal text1
# print('non local function output : ', text1)


# global_func()
# global text1
# print('global function output : ', text1)

# local_class_ex()
# print('global output : ', text1)


# here the first function defines a local variable text1 within its own scope. This local text1 can only be accessed within local_func
# second function it modifies the text1 variable that exists in the scope of local_class_ex
# third function modifies the global variable text1, which is defined outside any function. By using the global keyword, it allows changes to this global variable.



