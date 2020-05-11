from functools import wraps

exc = ''
class User:
    def exc_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                print(func(*args, **kwargs))
            except Exception as e:
                raise Exception(exc)
        return wrapper
   
            
    @exc_decorator
    def get_account_balance(self, balance):
        global exc
        self.balance = balance 
        print(self.balance)
    
    @exc_decorator
    def  change_password(self, password):
        global exc
        self.password = password
        print(self.password)
    

u = User()
u.get_account_balance()
u.change_password()
