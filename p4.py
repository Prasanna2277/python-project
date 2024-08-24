from tkinter import messagebox, simpledialog, Tk

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    return [message[i] for i in range(len(message)) if is_even(i)]

def get_odd_letters(message):
    return [message[i] for i in range(len(message)) if not is_even(i)]

def swap_letters(message):
    if not is_even(len(message)):
        message += 'x'  

    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    
    
    letter_list = []
    for i in range(len(even_letters)):
        letter_list.append(odd_letters[i] if i < len(odd_letters) else '')
        letter_list.append(even_letters[i] if i < len(even_letters) else '')

    return ''.join(letter_list)

def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt? (Type "encrypt" or "decrypt")')
    return task.strip().lower()

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message or ''

def main():
    root = Tk()
    root.withdraw()  
    while True:
        task = get_task()
        if task == 'encrypt':
            message = get_message()
            if message:
                encrypted = swap_letters(message)
                messagebox.showinfo('Ciphertext', encrypted)
        elif task == 'decrypt':
            message = get_message()
            if message:
                decrypted = swap_letters(message)
                messagebox.showinfo('Plaintext', decrypted)
        elif task in ['quit', 'exit']:
            break
        else:
            messagebox.showerror('Error', 'Invalid task. Please type "encrypt" or "decrypt".')
    root.mainloop()

if __name__ == "__main__":
    main()
