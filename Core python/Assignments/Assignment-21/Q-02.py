class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def input_data(self):
        self.model_number = int(input("Enter model number: "))
        self.screen_size = float(input("Enter screen size (in inches): "))
        self.price = float(input("Enter price (Rs.): "))

        # Validate model number
        if self.model_number < 0 or self.model_number > 9999:
            raise Exception("Model number must not have more than 4 digits.")

        # Validate screen size
        if self.screen_size < 12 or self.screen_size > 70:
            raise Exception("Screen size must be between 12 and 70 inches.")

        # Validate price
        if self.price < 0 or self.price > 5000:
            raise Exception("Price must be between Rs. 0 and Rs. 5000.")

    def display(self):
        print("\nTelevision Details")
        print("Model Number :", self.model_number)
        print("Screen Size  :", self.screen_size, "inches")
        print("Price        : Rs.", self.price)

    def reset(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

tv = Television()

try:
    tv.input_data()
    tv.display()
except Exception as e:
    print("\nException:", e)
    # Set all data members to zero
    tv.reset()
    print("\nAll data members have been set to zero.")
    tv.display()
