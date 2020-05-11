class User:
    def excpt_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                print(func(*args, **kwargs))
            except Exception as e:
                raise Exception('No username defined!')
        return wrapper
    
            
    @excpt_decorator
    def get_account_balance(self, balance):
        self.balance = balance 
        print(self.balance)
    
    @excpt_decorator
    def  change_password(self, password):
        self.password = password
        print(self.password)
    

u = User()
# u.get_account_balance()
# u.change_password()