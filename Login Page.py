import tkinter as tk
from tkinter import messagebox
import hashlib
import sqlite3
import secrets
import string



class LoginPage:
    def __init__(self, root):
        self.BG = "#082700"
        self.FG = "#FFFFFF"
        self.root = root
        self.root.resizable(False, False)
        self.root.configure(bg=self.BG)

        self.current_user = None

        self.initial_database()

        self.show_login_page()

    def show_login_page(self):
        self.clear_canvas()

        self.root.title("Login Page")
        self.root.geometry("400x330")
        self.user_log_info = tk.StringVar()
        self.pass_log_info = tk.StringVar()
        self.ENTRY_BG = "#83C274"



        frame = tk.Frame(self.root,bg=self.BG)
        frame.pack(padx=10)

        tk.Label(frame, text="Username:", font=("Arial", 18,'bold'),bg=self.BG, fg=self.FG).grid(row=0, column=0, padx=5, pady=10)
        tk.Entry(frame,textvariable=self.user_log_info, font=("Arial", 15), width=30,bg=self.ENTRY_BG).grid(row=1, column=0, padx=5, pady=10)


        tk.Label(frame, text="Password:",font=("Arial",18, 'bold'),bg=self.BG,fg=self.FG).grid(row=2, column=0,padx=5, pady=10)

        show_pass = tk.IntVar()

        pass_ent = tk.Entry(frame,textvariable=self.pass_log_info, font=("Arial", 15), width=30,bg=self.ENTRY_BG,show="*")
        pass_ent.grid(row=3, column=0,padx=5, pady=10)

        def toggle_pass():
            if show_pass.get():
                pass_ent.config(show="")
            else:
                pass_ent.config(show="*")


        self.BTN_BG ="#366A29"
        self.ACT_BTN_BG = "#6CCE53"
        button_frame = tk.Frame(self.root,bg=self.BG)
        button_frame.pack(padx=10)

        show_pass_cb = tk.Checkbutton(button_frame, text="Show Password",variable=show_pass,
                                           font=("Arial", 10),bg=self.BG,fg=self.FG,
                                           activeforeground=self.FG,selectcolor=self.BG,
                                           activebackground=self.BG, command=toggle_pass)
        show_pass_cb.grid(row=0, column=1 ,padx=5, pady=10)
        self.login_btn = tk.Button(button_frame, text="Login", font=("Arial", 12, "bold")
                                   ,bg=self.BTN_BG, fg=self.FG,borderwidth=0,width=8, activebackground=self.ACT_BTN_BG, activeforeground=self.FG, command=self.login)
        self.login_btn.grid(row=1, column=1, padx=10,pady=10)


        exit_btn = tk.Button(button_frame, text="Exit", font=("Arial", 12, "bold")
                                   ,bg=self.BTN_BG, fg=self.FG,borderwidth=0,width=7, activebackground=self.ACT_BTN_BG, activeforeground=self.FG, command=self.exit)
        exit_btn.grid(row=1, column=2, padx=10, pady=10)

        signin_btn = tk.Button(button_frame, text="Sign-In", font=("Arial", 12, "bold")
                                   ,bg=self.BTN_BG, fg=self.FG,borderwidth=0,width=8, activebackground=self.ACT_BTN_BG, activeforeground=self.FG, command=self.show_signin_page)
        signin_btn.grid(row=1, column=0, padx=10, pady=10)





    def clear_canvas(self):
        for widget in self.root.winfo_children():
            widget.destroy()



    def exit(self):
        self.root.destroy()
    def initial_database(self):
        self.conn = sqlite3.connect("login_info.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP
            )
        
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                data_key TEXT,
                data_value TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id),
                UNIQUE(user_id, data_key)
            )
        ''')

        self.conn.commit()




    def hash_password(self, password: str, salt="abcdef"):
        new_pass = (password + salt).encode()
        hashed_password = hashlib.sha3_384(new_pass).hexdigest()
        return hashed_password
    def show_signin_page(self):
        self.clear_canvas()
        self.user_info = tk.StringVar()
        self.pass_info = tk.StringVar()
        self.confirm_info = tk.StringVar()
        self.ENTRY_BG = "#83C274"

        self.root.geometry("400x430")
        self.root.title("Sign-In")

        frame = tk.Frame(self.root,bg=self.BG)
        frame.pack(padx=10)

        tk.Label(frame, text="Username:", font=("Arial", 18,'bold'),bg=self.BG, fg=self.FG).grid(row=0, column=0, padx=5, pady=10)
        tk.Entry(frame,textvariable=self.user_info, font=("Arial", 15), width=30,bg=self.ENTRY_BG).grid(row=1, column=0, padx=5, pady=10)

        tk.Label(frame, text="Password:",font=("Arial",18, 'bold'),bg=self.BG,fg=self.FG).grid(row=2, column=0,padx=5, pady=10)
        pass_ent = tk.Entry(frame,textvariable=self.pass_info, font=("Arial", 15), width=30,bg=self.ENTRY_BG,show="*")
        pass_ent.grid(row=3, column=0,padx=5, pady=10)

        tk.Label(frame, text="Confirm Password:",font=("Arial",18, 'bold'),bg=self.BG,fg=self.FG).grid(row=4, column=0,padx=5, pady=10)
        con_pass_ent =tk.Entry(frame,textvariable=self.confirm_info, font=("Arial", 15), width=30,bg=self.ENTRY_BG,show="*")
        con_pass_ent.grid(row=5, column=0,padx=5, pady=10)

        BTN_BG ="#366A29"
        ACT_BTN_BG = "#6CCE53"
        button_frame = tk.Frame(self.root,bg=self.BG)
        button_frame.pack(padx=10)

        login_btn = tk.Button(button_frame, text="Add Account", font=("Arial", 12, "bold")
                                   ,bg=self.BTN_BG, fg=self.FG,borderwidth=0,width=12, activebackground=self.ACT_BTN_BG, activeforeground=self.FG, command=self.signin)
        login_btn.grid(row=1, column=1, padx=10, pady=10)

        self.exit_btn = tk.Button(button_frame, text="Exit", font=("Arial", 12, "bold")
                                   ,bg=self.BTN_BG, fg=self.FG,borderwidth=0,width=7, activebackground=ACT_BTN_BG, activeforeground=self.FG, command=self.exit)
        self.exit_btn.grid(row=1, column=2, padx=10, pady=10)

        self.signin_btn = tk.Button(button_frame, text="Login", font=("Arial", 12, "bold")
                                   ,bg=self.BTN_BG, fg=self.FG,borderwidth=0,width=8, activebackground=ACT_BTN_BG, activeforeground=self.FG, command=self.show_login_page)
        self.signin_btn.grid(row=1, column=0, padx=10, pady=10)

        show_pass = tk.IntVar()
        show_pass.set(0)
        def toggle_pass():
            if show_pass.get():
               pass_ent.configure(show="")
               con_pass_ent.configure(show="")
            else:
                pass_ent.configure(show="*")
                con_pass_ent.configure(show="*")



        self.show_pass_cb = tk.Checkbutton(button_frame, text="Show Password",variable=show_pass,
                                           font=("Arial", 10),bg=self.BG,fg=self.FG,
                                           activeforeground=self.FG,selectcolor=self.BG,
                                           activebackground=self.BG, command=toggle_pass)

        self.show_pass_cb.grid(row=0, column=1, padx=10, pady=10)


    def signin(self):
        username = self.user_info.get().strip()
        password = self.pass_info.get().strip()
        confirm = self.confirm_info.get().strip()


        if len(username) < 3:
            messagebox.showerror("Error", "Username must be at least 3 characters")
            self.user_info.set("")
            return
        if password != confirm:
            messagebox.showerror("Error", "Password and Confirm Password must match")
            return
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters")
            return
        try:
            hashed_pass = self.hash_password(password)
            self.cursor.execute('''
            INSERT INTO users (username,password) VALUES (?,?)
            ''',(username,hashed_pass))
            self.conn.commit()

            messagebox.showinfo("Success", "Successfully Signed in")
            self.show_login_page()


        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")

    def login(self):
        username = self.user_log_info.get().strip()
        password = self.pass_log_info.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and Password must be entered")
            return

        hashed_pass = self.hash_password(password)
        self.cursor.execute('''
            SELECT id, username FROM users 
            WHERE username = ? AND password = ?
        ''', (username, hashed_pass))

        user = self.cursor.fetchone()

        if user:


            self.current_user = {'id' : user[0], 'username' : user[1]}
            self.cursor.execute('''
                SELECT id, username, created_at, last_login FROM users WHERE id = ?
            ''', (user[0],))
            updated_user = self.cursor.fetchone()

            self.current_user = {'id': updated_user[0], 'username': updated_user[1]}

            # Print login information to console
            print("\n" + "=" * 50)
            print("✅ SUCCESSFUL LOGIN DETECTED")
            print("=" * 50)
            print(f"User ID: {updated_user[0]}")
            print(f"Username: {updated_user[1]}")
            print(f"Account Created: {updated_user[2]}")
            print("=" * 50 + "\n")


            messagebox.showinfo("Success", f"Welcome {self.current_user['username']}")
            self.show_pass_panel()


        else:
            messagebox.showerror("Error", "Username or password is wrong")


    # def show_pass_panel(self):
    #     self.clear_canvas()
    #     self.root.geometry("500x500")
    #     self.root.title("Vault")
    #
    #     self.LIST_BG = "#3c6c40"
    #     vault_frame = tk.Frame(self.root,bg=self.BG)
    #     vault_frame.pack(padx=10,pady=10)
    #
    #     self.lbl_frame_pass = tk.LabelFrame(vault_frame,bg=self.LIST_BG)
    #     self.lbl_frame_pass.pack(padx=10,pady=10)
    #     self.scroly = tk.Scrollbar(self.lbl_frame_pass,orient="vertical")
    #     self.scroly.pack(side="right",fill="y")
    #     self.pass_list =tk.Listbox(self.lbl_frame_pass, selectbackground="#203b22",selectmode='single',font=('Arial', 12),fg= self.FG,bg=self.LIST_BG)
    #     self.pass_list.pack(fill="both",expand="yes")
    #
    #     self.scroly.config(command=self.pass_list.yview)
    #     self.update_panel()
    # def update_panel(self):
    #     self.pass_list.insert(tk.END,self.current_user['username'])


    def show_pass_panel(self):
        self.clear_canvas()
        self.root.geometry("500x650")
        self.root.title("Vault")

        self.LIST_BG = "#3c6c40"

        # Create main frame
        main_frame = tk.Frame(self.root, bg=self.BG)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create LabelFrame for user info
        user_frame = tk.LabelFrame(main_frame, text="User Information",
                                   font=("Arial", 12, "bold"),
                                   bg=self.BG, fg=self.FG,
                                   padx=10, pady=5)
        user_frame.pack(fill="x", pady=(0, 10))

        # Get user info from database
        self.cursor.execute('''
            SELECT username, last_login FROM users WHERE id = ?
        ''', (self.current_user['id'],))

        user_data = self.cursor.fetchone()

        if user_data:
            username = user_data[0]
            last_login = user_data[1]



            # Username label
            tk.Label(user_frame, text=f"Username: {username}",
                     font=("Arial", 11), bg=self.BG, fg=self.FG).pack(anchor="w", pady=2)


        # Create frame for listbox
        vault_frame = tk.Frame(main_frame, bg=self.BG)
        vault_frame.pack(fill="both", expand=True)

        self.scroly = tk.Scrollbar(vault_frame, orient="vertical")
        self.scroly.pack(side="right", fill="y")

        self.pass_list = tk.Listbox(vault_frame, selectbackground="#203b22",
                                    selectmode='single', font=('Arial', 12),
                                    fg=self.FG, bg=self.LIST_BG)
        self.pass_list.pack(fill="both", expand=True)

        self.scroly.config(command=self.pass_list.yview)

        button_frame = tk.Frame(main_frame, bg=self.BG)
        button_frame.pack(pady=10)

        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)

        self.add_btn = tk.Button(button_frame, text="Add a password", font=("Arial", 11)
                                   ,bg=self.BTN_BG, fg=self.FG,borderwidth=0,width=13, activebackground=self.ACT_BTN_BG, activeforeground=self.FG,command=self.add_pass)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.edit_btn = tk.Button(button_frame, text="Edit", font=("Arial", 11),
                                  bg=self.BTN_BG, fg=self.FG,borderwidth=0,width=13, activebackground=self.ACT_BTN_BG, activeforeground=self.FG,command=self.edit_pass)
        self.edit_btn.grid(row=0, column=1, padx=5)

        self.copy_btn = tk.Button(button_frame, text="Copy", font=("Arial", 11),
                                  bg=self.BTN_BG, fg=self.FG,borderwidth=0,width=13, activebackground=self.ACT_BTN_BG, activeforeground=self.FG,command=self.copy)
        self.copy_btn.grid(row=0, column=2, padx=10)

        self.logout_btn = tk.Button(button_frame, text="Logout", font=("Arial", 11)
                              , bg=self.BTN_BG, fg=self.FG, borderwidth=0, width=7, activebackground=self.ACT_BTN_BG,
                               activeforeground=self.FG, command=self.logout)
        self.logout_btn.grid(row=1, column=1, padx=10, pady=10)


        self.update_panel()
    def logout(self):
        self.clear_canvas()
        self.current_user = None
        self.show_login_page()




    def update_panel(self):
        """Update the listbox with stored passwords"""
        self.pass_list.delete(0, tk.END)  # Clear existing items

        # Get passwords from user_data table
        self.cursor.execute('''
            SELECT data_key, data_value FROM user_data 
            WHERE user_id = ?
        ''', (self.current_user['id'],))

        passwords = self.cursor.fetchall()

        if passwords:
            for service, password in passwords:
                self.pass_list.insert(tk.END, f"{service}|||{password}")

        # if passwords:
        #     for service, password in passwords:
        #         self.pass_list.insert(tk.END, f"Service: {service}")
        #         self.pass_list.insert(tk.END, f"Password: {password}")
        #         self.pass_list.insert(tk.END, "-" * 40)
        else:
            self.pass_list.insert(tk.END, "No passwords stored yet")

    def add_pass(self):
        win = tk.Toplevel(self.root)
        win.title("Add Password")
        win.resizable(False, False)
        win.geometry("300x260")
        win.configure(bg=self.BG)

        self.ser_info = tk.StringVar()
        self.pass_info_add = tk.StringVar()
        tk.Label(win, text="Service", bg=self.BG,fg = self.FG,font=('Arial',12)).pack(padx=5, pady=5)
        service = tk.Entry(win,textvariable=self.ser_info, font=("Arial", 12), width=30,bg=self.ENTRY_BG)
        service.pack(padx=5, pady=10)

        tk.Label(win,  text="Password", bg=self.BG,fg = self.FG,font=('Arial',12)).pack(padx=5, pady=5)
        password = tk.Entry(win,textvariable=self.pass_info_add, font=("Arial", 12), width=30,bg=self.ENTRY_BG)
        password.pack(padx=5, pady=10)



        def save():
            if not service.get() or not password.get():
                messagebox.showerror("Error", "Please fill all fields")
                return

            service_name = service.get().strip()
            password_value = password.get().strip()

            if not service_name :
                messagebox.showerror("Error", "Service name cannot be empty")
                return
            if service.get().startswith(" "):
                messagebox.showerror("Error", "Service name cannot start with space")
                return


            self.cursor.execute('''
                SELECT * FROM user_data 
                WHERE user_id = ? AND data_key = ?
            ''', (self.current_user['id'], service.get()))

            existing = self.cursor.fetchone()
            if existing:
                messagebox.showerror("Error", "Service already exists")
                return

            self.cursor.execute('''
            INSERT INTO user_data (user_id, data_key, data_value) VALUES (?, ?, ?)
            ''', (self.current_user['id'],service_name,password_value))


            self.conn.commit()
            win.destroy()
            self.update_panel()




        def generate_pass_panel():
            win_gen = tk.Toplevel(self.root)
            win_gen.title("Generate Password")
            win_gen.resizable(False, False)
            win_gen.geometry("400x200")
            win_gen.configure(bg=self.BG)


            option_list = ["Simple","Hard","Extreme"]


            value_inside = tk.StringVar(win_gen)
            value_inside.set("Select the difficulty")



            gen_frame = tk.Frame(win_gen, bg=self.BG)
            gen_frame.pack(padx=5, pady=5)
            diff = tk.OptionMenu(gen_frame, value_inside, *option_list)
            diff.config(bg="#1e6d11", fg=self.FG, font=("Arial", 12),bd=0,activebackground="#37c322",activeforeground=self.FG)
            diff.grid(row=0, column=0, padx=20, pady=20)



            menu = diff["menu"]
            menu.config(bg="#1e6d11", fg=self.FG, font=("Arial", 12),borderwidth=0,activebackground="#37c322",activeforeground=self.FG)
            self.gen_length_sv = tk.StringVar()
            self.gen_length_sv.set("Length...")


            gen_entry = tk.Entry(gen_frame, textvariable=self.gen_length_sv, font=("Arial", 12), width=8, bg=self.ENTRY_BG,fg="#2D2D2D",justify="center")
            gen_entry.grid(row=0, column=1, padx=20, pady=20)
            self.output_val = tk.StringVar()
            gen_output = tk.Label(gen_frame, textvariable=self.output_val,font=("Arial", 10), width=45, bg=self.ENTRY_BG,fg="Black")
            gen_output.grid(row=1, column=0,columnspan=2,pady=10)

            def del_ph(even=None):
                if self.gen_length_sv.get() == "Length...":
                    gen_entry.delete(0, tk.END)
                    gen_entry.config(fg="black")

            def on_focus_out(event=None):
                if self.gen_length_sv.get() == "":
                    self.gen_length_sv.set("Length...")
                    gen_entry.config(fg="#2D2D2D")

            def validate_k(event=None):
                current = self.gen_length_sv.get()
                if current and current != "Length...":  # Fixed: case sensitivity
                    if not current.isdigit():
                        digits_only = ''.join(filter(str.isdigit, current))
                        self.gen_length_sv.set(digits_only)
                        if digits_only:
                            gen_entry.config(fg="Black")

            gen_entry.bind("<FocusIn>", del_ph)
            gen_entry.bind("<FocusOut>", on_focus_out)
            gen_entry.bind("<KeyRelease>", validate_k)


            self.generated_pass = tk.StringVar()
            def generate():
                try:
                    length = int(self.gen_length_sv.get())
                    if length < 0:
                        messagebox.showerror("Error", "Password too short")


                    if value_inside.get() == "Simple":
                        if length >32:
                            messagebox.showwarning("Password too long","At most 32 characters")
                        elif length >= 6:
                            alphabet_simple = string.digits
                            a = ''.join(secrets.choice(alphabet_simple) for _ in range(int(self.gen_length_sv.get())))
                            self.output_val.set(a)
                            self.generated_pass.set(a)
                        else:
                            messagebox.showwarning("Password too long","At least 6 character")


                    elif value_inside.get() == "Hard":
                        if length > 32:
                            messagebox.showwarning("Password too long","At most 32 characters")
                        elif length >=6 :
                            alphabet_simple = string.digits + string.ascii_letters
                            a = ''.join(secrets.choice(alphabet_simple) for _ in range(int(self.gen_length_sv.get())))
                            self.output_val.set(a)
                            self.generated_pass.set(a)
                        else:
                            messagebox.showwarning("Password too short","At least 6 characters")


                    elif value_inside.get() == "Extreme":
                        if length > 32:
                            messagebox.showwarning("Password too long", "At most 32 characters")
                        elif length >= 8:
                            alphabet_simple = string.ascii_letters + string.digits + string.punctuation
                            a = ''.join(secrets.choice(alphabet_simple) for _ in range(int(self.gen_length_sv.get())))
                            self.output_val.set(a)
                            self.generated_pass.set(a)
                        else:
                            messagebox.showwarning("Password too short", "At least 8 characters")


                except ValueError:
                    messagebox.showerror("Error", "How Long?")
                except Exception:
                    messagebox.showerror("Error", f"Something Went Wrong{str(Exception)}")

            def copy_pass():
                password = self.generated_pass.get()
                if password:
                    gen_frame.clipboard_clear()
                    gen_frame.clipboard_append(self.generated_pass.get())
                else:
                    messagebox.showerror("Error", "No Password")

            generate_p = tk.Button(gen_frame, text="Generate", font=("Arial", 10),
                                      bg=self.BTN_BG, fg=self.FG, borderwidth=0, width=12,
                                      activebackground=self.ACT_BTN_BG, activeforeground=self.FG,
                                      command=generate)
            generate_p.grid(row=2, column=0, padx=10, pady=20)

            generate_p = tk.Button(gen_frame, text="Copy", font=("Arial", 8),
                                      bg=self.BTN_BG, fg=self.FG, borderwidth=0, width=5,
                                      activebackground=self.ACT_BTN_BG, activeforeground=self.FG,
                                      command=copy_pass)
            generate_p.grid(row=2, column=1, padx=10, pady=20)



        btn_frame = tk.Frame(win, bg=self.BG)
        btn_frame.pack(pady=10)

        save = tk.Button(btn_frame, text="Save", font=("Arial", 11),
              bg=self.BTN_BG, fg=self.FG,borderwidth=0,width=8, activebackground=self.ACT_BTN_BG, activeforeground=self.FG, command=save)
        save.grid(row=0, column=0,padx=10 ,pady=5)

        cancel = tk.Button(btn_frame, text="Cancel", font=("Arial", 11),
              bg=self.BTN_BG, fg=self.FG,borderwidth=0,width=8, activebackground=self.ACT_BTN_BG, activeforeground=self.FG,command=win.destroy)
        cancel.grid(row=0, column=1,padx=10,pady=5)

        generate_pass = tk.Button(btn_frame, text="Generate", font=("Arial", 10),
              bg=self.BTN_BG, fg=self.FG,borderwidth=0,width=12, activebackground=self.ACT_BTN_BG, activeforeground=self.FG,command=generate_pass_panel)
        generate_pass.grid(row=1, column=0,columnspan=2, padx=10, pady=20)


    def edit_pass(self):
        selected = self.pass_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Select to edit")
            return

        selected_text = self.pass_list.get(selected[0])
        parts = selected_text.split("|||", 1)
        if len(parts) != 2:
            messagebox.showerror("Error", "Invalid format")
            return


        old_service = parts[0].strip()
        old_password = parts[1].strip()


        self.cursor.execute('''
            SELECT data_key, data_value FROM user_data 
            WHERE user_id = ? AND data_key = ?
        ''', (self.current_user['id'], old_service))

        result = self.cursor.fetchone()
        if not result:
            messagebox.showerror("Error", "Password not found")
            return
        old_service = result[0]
        old_password = result[1]

        win = tk.Toplevel(self.root)
        win.title("Edit Password")
        win.resizable(False, False)
        win.geometry("300x200")
        win.configure(bg=self.BG)

        ser_info = tk.StringVar()
        pass_info_add = tk.StringVar()
        ser_info.set(old_service)
        pass_info_add.set(old_password)
        tk.Label(win, text="Service", bg=self.BG,fg = self.FG,font=('Arial',12)).pack(padx=5, pady=5)
        service_entry = tk.Entry(win,textvariable=ser_info, font=("Arial", 12), width=30,bg=self.ENTRY_BG)
        service_entry.pack(padx=5, pady=10)

        tk.Label(win,  text="Password", bg=self.BG,fg = self.FG,font=('Arial',12)).pack(padx=5, pady=5)
        password_entry = tk.Entry(win,textvariable=pass_info_add, font=("Arial", 12), width=30,bg=self.ENTRY_BG)
        password_entry.pack(padx=5, pady=10)

        def save():
            new_service = service_entry.get().strip()
            new_password = password_entry.get().strip()

            if not new_service or not new_password:
                messagebox.showerror("Error", "Please fill all fields")
                return

            # Check if new service name conflicts with another service
            if new_service != old_service:
                self.cursor.execute('''
                    SELECT * FROM user_data 
                    WHERE user_id = ? AND data_key = ?
                ''', (self.current_user['id'], new_service))

                if self.cursor.fetchone():
                    messagebox.showerror("Error", f"Service '{new_service}' already exists!")
                    return

            # Update the password
            self.cursor.execute('''
                UPDATE user_data 
                SET data_key = ?, data_value = ?, updated_at = CURRENT_TIMESTAMP
                WHERE user_id = ? AND data_key = ?
            ''', (new_service, new_password, self.current_user['id'], old_service))

            self.conn.commit()
            win.destroy()
            self.update_panel()
        def delete():
            service = service_entry.get().strip()

            confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this service?")
            if confirm:
                self.cursor.execute('''
                DELETE FROM user_data WHERE user_id = ? AND data_key = ? 
                ''',(self.current_user['id'], service))

                self.conn.commit()
                self.update_panel()
                win.destroy()

        btn_frame = tk.Frame(win, bg=self.BG)
        btn_frame.pack(pady=10)

        save_btn = tk.Button(btn_frame, text="Update", font=("Arial", 11),
                             bg=self.BTN_BG, fg=self.FG, borderwidth=0, width=8,
                             activebackground=self.ACT_BTN_BG, activeforeground=self.FG,
                             command=save)
        save_btn.grid(row=0, column=0, padx=10)

        cancel_btn = tk.Button(btn_frame, text="Delete", font=("Arial", 11),
                               bg=self.BTN_BG, fg=self.FG, borderwidth=0, width=8,
                               activebackground=self.ACT_BTN_BG, activeforeground=self.FG,
                               command=delete)
        cancel_btn.grid(row=0, column=2, padx=10)


        delete_btn = tk.Button(btn_frame, text="Cancel", font=("Arial", 11),
                               bg=self.BTN_BG, fg=self.FG, borderwidth=0, width=8,
                               activebackground=self.ACT_BTN_BG, activeforeground=self.FG, command=win.destroy)
        delete_btn.grid(row=0, column=1, padx=10)

    def copy(self):
        selected = self.pass_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Select to copy")
            return

        selected_text = self.pass_list.get(selected[0])
        parts = selected_text.split("|||",1)
        if len(parts) != 2:
            messagebox.showerror("Error", "Invalid format")
            return
        password = parts[1].strip()




        self.root.clipboard_clear()
        self.root.clipboard_append(password)

        messagebox.showinfo("Success", "Password copied to clipboard")





if __name__ == "__main__":
    root = tk.Tk()
    logging = LoginPage(root)
    root.mainloop()


