import tkinter as tk
from tkinter import messagebox

class Email:
    def __init__(self, subject, sender, body):
        self.subject = subject
        self.sender = sender
        self.body = body

class EmailFilter:
    def __init__(self, keywords):
        self.keywords = keywords

    def filter_emails(self, emails):
        filtered_emails = []
        for email in emails:
            if self.is_spam(email):
                print(f"Spam email detected: Subject - {email.subject}, Sender - {email.sender}")
            else:
                filtered_emails.append(email)
        return filtered_emails

    def is_spam(self, email):
        for keyword in self.keywords:
            if keyword in email.subject.lower() or keyword in email.body.lower():
                return True
        return False

def filter_emails_gui():
    keywords = entry_keywords.get().split(',')
    emails = [
        Email('Important Update', 'john.doe@example.com', 'Please find the attached report.'),
        Email('Claim Your Prize!', 'winner@example.com', 'Congratulations! You have won a free vacation.'),
        Email('Meeting Agenda', 'team@example.com', 'Agenda for the upcoming meeting.'),
        Email('Important Information', 'info@example.com', 'Please review the attached document.'),
        Email('You Won $1 Million!', 'lotterywinner@example.com', 'Claim your prize now!'),
    ]

    email_filter = EmailFilter(keywords)
    filtered_emails = email_filter.filter_emails(emails)

    filtered_emails_text = "\nFiltered Emails:\n"
    for email in filtered_emails:
        filtered_emails_text += f"Subject: {email.subject}, Sender: {email.sender}\n"

    messagebox.showinfo("Filtered Emails", filtered_emails_text)

# GUI setup
root = tk.Tk()
root.title("Email Filter")
root.geometry("400x200")

label_keywords = tk.Label(root, text="Enter keywords separated by commas:")
label_keywords.pack()

entry_keywords = tk.Entry(root)
entry_keywords.pack()

filter_button = tk.Button(root, text="Filter Emails", command=filter_emails_gui)
filter_button.pack()

root.mainloop()
