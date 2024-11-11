class SecretCode:
    def __init__(self, initial_code):
        try:
            self.code = initial_code
        except Exception as e:
            print(f"Error initializing Secraet Code: {e}")

    def get_code(self):
        try:
            return self.code
        except Exception as e:
            print(f"Error getting code: {e}")
            return None
        
    def set_code(self, new_code):
        try:
            self.code = new_code
        except Exception as e:
            print(f"Error setting code: {e}")