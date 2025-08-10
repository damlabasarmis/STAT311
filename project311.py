import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog
import pymysql


# Database connection setup
def initialize_db():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="student",
        database="moviewatchlist"
    )
    return connection


# Main App Class
class MovieWatchlistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Watchlist")
        self.root.geometry("800x600")
        self.db = initialize_db()

        # Color scheme
        self.colors = {
            "bg": "#f8ede3",
            "fg": "#6b4c35",
            "button": "#d6ccc2",
            "entry_bg": "#e3d5ca",
            "highlight": "#c3a995",
        }

        # Login Page
        self.create_login_page()

    def create_login_page(self):
        self.clear_window()

        tk.Label(self.root, text="Welcome to Movie Watchlist", font=("Helvetica", 16), bg=self.colors["bg"],
                 fg=self.colors["fg"]).pack(pady=20)

        frame = tk.Frame(self.root, bg=self.colors["bg"])
        frame.pack(pady=20)

        tk.Label(frame, text="Username:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=0, column=0, padx=10,
                                                                                           pady=10)
        self.username_entry = tk.Entry(frame, bg=self.colors["entry_bg"], fg=self.colors["fg"])
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame, text="Password:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=1, column=0, padx=10,
                                                                                           pady=10)
        self.password_entry = tk.Entry(frame, show="*", bg=self.colors["entry_bg"], fg=self.colors["fg"])
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Log In", command=self.login, bg=self.colors["button"], fg=self.colors["fg"]).pack(
            pady=10)
        tk.Button(self.root, text="Register", command=self.create_register_page, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        cursor = self.db.cursor()
        query = "SELECT * FROM USER WHERE Username = %s AND Password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()#???????? to avoid error?? if there multiple users
        if result:
            self.user_id = result[0]
            messagebox.showinfo("Login", f"Welcome, {username}!")
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def create_register_page(self):
        self.clear_window()

        tk.Label(self.root, text="Register to Movie Watchlist", font=("Helvetica", 16), bg=self.colors["bg"],
                 fg=self.colors["fg"]).pack(pady=20)

        frame = tk.Frame(self.root, bg=self.colors["bg"])
        frame.pack(pady=20)

        tk.Label(frame, text="Username:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=0, column=0, padx=10,
                                                                                           pady=10)
        self.rusername_entry = tk.Entry(frame, bg=self.colors["entry_bg"], fg=self.colors["fg"])
        self.rusername_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame, text="Email:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=1, column=0, padx=10,
                                                                                        pady=10)
        self.remail_entry = tk.Entry(frame, bg=self.colors["entry_bg"], fg=self.colors["fg"])
        self.remail_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(frame, text="Password:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=2, column=0, padx=10,
                                                                                           pady=10)
        self.rpassword_entry = tk.Entry(frame, show="*", bg=self.colors["entry_bg"], fg=self.colors["fg"])
        self.rpassword_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Register", command=self.register, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

        tk.Button(self.root, text="Update Account", command=self.update_account, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

        tk.Button(self.root, text="Delete Account", command=self.delete_account, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

        tk.Button(self.root, text="Back", command=self.create_login_page, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

    def register(self):
        username = self.rusername_entry.get()
        password = self.rpassword_entry.get()
        email=self.remail_entry.get()
        cursor = self.db.cursor()
        query="INSERT INTO USER(Username, Password,Email) VALUES (%s, %s,%s)"

        try:
            cursor.execute(query, (username, password, email))
            self.db.commit()
            messagebox.showinfo("Success", "User successfully registered.")
        except Exception as e:
            messagebox.showerror("Error", "Could not register user.")

    def update_account(self):
        username = self.rusername_entry.get()
        email = self.remail_entry.get()
        new_password = self.rpassword_entry.get()

        if not username or not email or not new_password:
            messagebox.showwarning("Missing Information", "All fields are required to update the account.")
            return

        cursor = self.db.cursor()
        query = "UPDATE USER SET Username = %s, Password = %s WHERE Email = %s"

        try:
            cursor.execute(query, (username, new_password, email))
            self.db.commit()
            messagebox.showinfo("Success", "Account updated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not update account: {e}")

    def delete_account(self):
        email = self.remail_entry.get()

        if not email:
            messagebox.showwarning("Missing Information", "Email is required to delete the account.")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this account?")
        if not confirm:
            return

        cursor = self.db.cursor()
        query = "DELETE FROM USER WHERE Email = %s"

        try:
            cursor.execute(query, (email,))
            self.db.commit()
            messagebox.showinfo("Success", "Account deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete account: {e}")

    def create_main_menu(self):
        self.clear_window()

        tk.Label(self.root, text="Main Menu", font=("Helvetica", 16), bg=self.colors["bg"], fg=self.colors["fg"]).pack(
            pady=20)

        tk.Button(self.root, text="View Movies", command=self.view_movies, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Manage Watchlist", command=self.manage_watchlist, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Explore Reviews", command=self.explore_reviews, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Explore Watchlists", command=self.explore_watchlists, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Learn About Directors", command=self.explore_directors, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Explore Platforms", command=self.explore_platforms, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Explore Genres", command=self.explore_genres, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Sign Out", command=self.create_login_page, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, bg=self.colors["button"], fg=self.colors["fg"]).pack(
            pady=10)

    def view_movies(self):
        self.clear_window()
        tk.Label(self.root, text="Movies", font=("Helvetica", 16), bg=self.colors["bg"], fg=self.colors["fg"]).pack(
            pady=20)

        tk.Button(self.root, text="Search by Platform", command=self.search_byplatform, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(side="top")
        tk.Button(self.root, text="Search by Genre", command=self.search_bygenre, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(side="top")
        tk.Button(self.root, text="Search by Director", command=self.search_bydirector, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(side="top")
        tk.Button(self.root, text="Search by Ratings", command=self.search_byrating, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(side="top")
        tk.Button(self.root, text="Back", command=self.create_main_menu, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(side="top")

        cursor = self.db.cursor()
        query = "SELECT Movie_id, Title, Run_time, Release_year FROM MOVIE"
        cursor.execute(query)
        movies = cursor.fetchall()

        frame1 = tk.Frame(self.root, bg=self.colors["bg"])
        frame1.pack(side="top")

        tree = ttk.Treeview(frame1, columns=("Movie_id", "Title", "Run_time", "Release_year"), show="headings")
        tree.heading("Movie_id", text="ID")
        tree.heading("Title", text="Title")
        tree.heading("Run_time", text="Run Time in minutes")
        tree.heading("Release_year", text="Release Year")

        for movie in movies:
            tree.insert("", "end", values=movie)
        tree.pack(side="top")

        # Buttons for Insert, Update, Delete
        tk.Button(self.root, text="Add Movie", command=self.add_movie, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(
            pady=5)
        tk.Button(self.root, text="Update Movie", command=lambda: self.update_movie(tree), bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=5)
        tk.Button(self.root, text="Delete Movie", command=lambda: self.delete_movie(tree), bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=5)

    def add_movie(self):
        def submit():
            title = title_entry.get()
            runtime = runtime_entry.get()
            release_year = release_year_entry.get()

            cursor = self.db.cursor()
            query = "INSERT INTO MOVIE (Title, Run_time, Release_year) VALUES (%s, %s, %s)"
            try:
                cursor.execute(query, (title, runtime, release_year))
                self.db.commit()
                messagebox.showinfo("Success", "Movie added successfully.")
                add_window.destroy()
                self.view_movies()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add movie: {e}")

        add_window = tk.Toplevel(self.root)
        add_window.title("Add Movie")

        tk.Label(add_window, text="Title:").pack()
        title_entry = tk.Entry(add_window)
        title_entry.pack()

        tk.Label(add_window, text="Run Time (minutes):").pack()
        runtime_entry = tk.Entry(add_window)
        runtime_entry.pack()

        tk.Label(add_window, text="Release Year:").pack()
        release_year_entry = tk.Entry(add_window)
        release_year_entry.pack()

        tk.Button(add_window, text="Submit", command=submit).pack(pady=10)

    def update_movie(self, tree):
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a movie to update.")
            return

        movie_data = tree.item(selected_item, "values")

        def submit():
            new_title = title_entry.get()
            new_runtime = runtime_entry.get()
            new_release_year = release_year_entry.get()

            cursor = self.db.cursor()
            query = "UPDATE MOVIE SET Title = %s, Run_time = %s, Release_year = %s WHERE Movie_id = %s"
            try:
                cursor.execute(query, (new_title, new_runtime, new_release_year, movie_data[0]))
                self.db.commit()
                messagebox.showinfo("Success", "Movie updated successfully.")
                update_window.destroy()
                self.view_movies()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update movie: {e}")

        update_window = tk.Toplevel(self.root)
        update_window.title("Update Movie")

        tk.Label(update_window, text="Title:").pack()
        title_entry = tk.Entry(update_window)
        title_entry.insert(0, movie_data[1])
        title_entry.pack()

        tk.Label(update_window, text="Run Time (minutes):").pack()
        runtime_entry = tk.Entry(update_window)
        runtime_entry.insert(0, movie_data[2])
        runtime_entry.pack()

        tk.Label(update_window, text="Release Year:").pack()
        release_year_entry = tk.Entry(update_window)
        release_year_entry.insert(0, movie_data[3])
        release_year_entry.pack()

        tk.Button(update_window, text="Submit", command=submit).pack(pady=10)

    def delete_movie(self, tree):
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a movie to delete.")
            return

        movie_data = tree.item(selected_item, "values")
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete movie '{movie_data[1]}'?")

        if not confirm:
            return

        cursor = self.db.cursor()
        query = "DELETE FROM MOVIE WHERE Movie_id = %s"
        try:
            cursor.execute(query, (movie_data[0],))
            self.db.commit()
            messagebox.showinfo("Success", "Movie deleted successfully.")
            self.view_movies()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete movie: {e}")

    def search_byplatform(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg=self.colors["bg"])
        frame.pack(pady=20)

        tk.Label(frame, text="Platform Name", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=0, column=0, padx=10,
                                                                                           pady=10)
        self.platform_entry = tk.Entry(frame, bg=self.colors["entry_bg"], fg=self.colors["fg"])
        self.platform_entry.grid(row=0, column=1, padx=10, pady=10)


        tk.Button(self.root, text="Search", command=self.platform, bg=self.colors["button"], fg=self.colors["fg"]).pack(
            pady=10)
        tk.Button(self.root, text="Back", command=self.view_movies, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

    def platform(self):
        search = self.platform_entry.get()
        cursor = self.db.cursor()
        query = "SELECT p.Platform_name,m.Title FROM MOVIE m JOIN PLATFORM p ON m.Movie_id=p.Movie_id WHERE %s = Platform_name"
        cursor.execute(query, search)
        movies = cursor.fetchall()#???????? to avoid error?? if there multiple users
        if movies:
            self.clear_window()
            tree = ttk.Treeview(self.root, columns=("Platform_name", "Title"), show="headings")
            tree.heading("Platform_name", text="Platform")
            tree.heading("Title", text="Movie")

            for movie in movies:
                tree.insert("", "end", values=movie)
            tree.pack(fill=tk.BOTH, expand=True)

            tk.Button(self.root, text="Back", command=self.search_byplatform, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=10)
        else:
            messagebox.showerror("Error", "Invalid platform name.")

    def search_bygenre(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg=self.colors["bg"])
        frame.pack(pady=20)

        tk.Label(frame, text="Genre", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=0, column=0, padx=10,
                                                                                               pady=10)
        self.genre_entry = tk.Entry(frame, bg=self.colors["entry_bg"], fg=self.colors["fg"])
        self.genre_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Search", command=self.genre, bg=self.colors["button"], fg=self.colors["fg"]).pack(
            pady=10)
        tk.Button(self.root, text="Back", command=self.view_movies, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

    def genre(self):
        search = self.genre_entry.get()
        cursor = self.db.cursor()
        query = "SELECT g.Name,m.Title FROM MOVIE m JOIN GENRE g ON m.Movie_id=g.Movie_id WHERE %s = g.Name"
        cursor.execute(query, search)
        movies = cursor.fetchall()  # ???????? to avoid error?? if there multiple users
        if movies:
            self.clear_window()
            tree = ttk.Treeview(self.root, columns=("Name", "Title"), show="headings")
            tree.heading("Name", text="Genre")
            tree.heading("Title", text="Movie")

            for movie in movies:
                tree.insert("", "end", values=movie)
            tree.pack(fill=tk.BOTH, expand=True)

            tk.Button(self.root, text="Back", command=self.search_bygenre, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=10)
        else:
            messagebox.showerror("Error", "Invalid genre name.")

    def search_bydirector(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg=self.colors["bg"])
        frame.pack(pady=20)

        tk.Label(frame, text="Director", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=0, column=0, padx=10,
                                                                                               pady=10)
        self.director_entry = tk.Entry(frame, bg=self.colors["entry_bg"], fg=self.colors["fg"])
        self.director_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Search", command=self.director, bg=self.colors["button"], fg=self.colors["fg"]).pack(
            pady=10)
        tk.Button(self.root, text="Back", command=self.view_movies, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

    def director(self):
        search = self.director_entry.get()
        cursor = self.db.cursor()
        query = "SELECT d.Name,m.Title FROM MOVIE m JOIN DIRECTOR d ON m.Movie_id=d.Movie_id WHERE %s = d.Name"
        cursor.execute(query, search)
        movies = cursor.fetchall()
        if movies:
            self.clear_window()
            tree = ttk.Treeview(self.root, columns=("Name", "Title"), show="headings")
            tree.heading("Name", text="Director")
            tree.heading("Title", text="Movie")

            for movie in movies:
                tree.insert("", "end", values=movie)
            tree.pack(fill=tk.BOTH, expand=True)

            tk.Button(self.root, text="Back", command=self.search_bydirector, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=10)
        else:
            messagebox.showerror("Error", "Invalid director name.")

    def search_byrating(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg=self.colors["bg"])
        frame.pack(pady=20)

        tk.Label(frame, text="Rating Above", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=0, column=0, padx=10,
                                                                                               pady=10)
        self.rating_entry = tk.Entry(frame, bg=self.colors["entry_bg"], fg=self.colors["fg"])
        self.rating_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Search", command=self.rating, bg=self.colors["button"], fg=self.colors["fg"]).pack(
            pady=10)
        tk.Button(self.root, text="Back", command=self.view_movies, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

    def rating(self):
            search = self.rating_entry.get()
            cursor = self.db.cursor()
            query = "SELECT r.Rating,m.Title FROM MOVIE m JOIN REVİEW r ON m.Movie_id=r.Movie_id WHERE %s < r.Rating"
            cursor.execute(query, int(search))
            movies = cursor.fetchall()  # ???????? to avoid error?? if there multiple users
            if movies:
                self.clear_window()
                tree = ttk.Treeview(self.root, columns=("Rating", "Title"), show="headings")
                tree.heading("Rating", text="Rating")
                tree.heading("Title", text="Movie")

                for movie in movies:
                    tree.insert("", "end", values=movie)
                tree.pack(fill=tk.BOTH, expand=True)

                tk.Button(self.root, text="Back", command=self.search_byrating, bg=self.colors["button"],
                          fg=self.colors["fg"]).pack(pady=10)
            else:
                messagebox.showerror("Error", "Invalid rating, enter 0-10.")
    def manage_watchlist(self):
        self.clear_window()
        tk.Label(self.root, text="Manage Watchlist", font=("Helvetica", 16), bg=self.colors["bg"],
                 fg=self.colors["fg"]).pack(pady=20)

        tk.Label(self.root, text="Add Movie to Watchlist", bg=self.colors["bg"], fg=self.colors["fg"]).pack(pady=20)

        frame = tk.Frame(self.root, bg=self.colors["bg"])
        frame.pack(pady=10)

        tk.Label(frame, text="Movie ID:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=0, column=0, padx=10,
                                                                                           pady=5)
        movie_id_entry = tk.Entry(frame, bg=self.colors["entry_bg"], fg=self.colors["fg"])
        movie_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Watchlist ID:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=1, column=0, padx=10,
                                                                                               pady=5)
        watchlist_entry = tk.Entry(frame, bg=self.colors["entry_bg"], fg=self.colors["fg"])
        watchlist_entry.grid(row=1, column=1, padx=10, pady=5)

        def add_to_watchlist():
            movie_id = movie_id_entry.get()
            watchlist_id=watchlist_entry.get()
            cursor = self.db.cursor()
            query = "INSERT INTO WATCHLIST_MOVIE(Movie_id,Watchlist_id) VALUES (%s,%s)"
            try:
                cursor.execute(query, (movie_id,watchlist_id))
                self.db.commit()
                messagebox.showinfo("Success", "Movie added to watchlist!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not add movie: {e}")

        tk.Button(frame, text="Add", command=add_to_watchlist, bg=self.colors["button"], fg=self.colors["fg"]).grid(
            row=0, column=2, padx=10, pady=5)

        def delete_from_watchlist():
            def submit():
                movie_id = movie_id_entry.get().strip()
                watchlist_id = watchlist_id_entry.get().strip()
                if not movie_id or not watchlist_id:
                    messagebox.showwarning("Invalid Input", "Both fields are required.")
                    return

                cursor = self.db.cursor()
                query = "DELETE FROM WATCHLIST_MOVIE WHERE Movie_id = %s AND Watchlist_id = %s"
                try:
                    cursor.execute(query, (movie_id, watchlist_id))
                    self.db.commit()
                    messagebox.showinfo("Success", "Movie removed from watchlist!")
                    delete_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Could not remove movie from watchlist: {e}")

            delete_window = tk.Toplevel(self.root)
            delete_window.title("Delete Movie from Watchlist")

            tk.Label(delete_window, text="Movie ID:").pack(pady=5)
            movie_id_entry = tk.Entry(delete_window)
            movie_id_entry.pack(pady=5)

            tk.Label(delete_window, text="Watchlist ID:").pack(pady=5)
            watchlist_id_entry = tk.Entry(delete_window)
            watchlist_id_entry.pack(pady=5)

            tk.Button(delete_window, text="Submit", command=submit).pack(pady=10)

        def update_watchlist_movie():
            def submit():
                movie_id = movie_id_entry.get().strip()
                new_watchlist_id = new_watchlist_id_entry.get().strip()
                if not movie_id or not new_watchlist_id:
                    messagebox.showwarning("Invalid Input", "Both fields are required.")
                    return

                cursor = self.db.cursor()
                query = "UPDATE WATCHLIST_MOVIE SET Watchlist_id = %s WHERE Movie_id = %s"
                try:
                    cursor.execute(query, (new_watchlist_id, movie_id))
                    self.db.commit()
                    messagebox.showinfo("Success", "Watchlist-Movie association updated!")
                    update_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Could not update association: {e}")

            update_window = tk.Toplevel(self.root)
            update_window.title("Update Watchlist-Movie Association")

            tk.Label(update_window, text="Movie ID:").pack(pady=5)
            movie_id_entry = tk.Entry(update_window)
            movie_id_entry.pack(pady=5)

            tk.Label(update_window, text="New Watchlist ID:").pack(pady=5)
            new_watchlist_id_entry = tk.Entry(update_window)
            new_watchlist_id_entry.pack(pady=5)

            tk.Button(update_window, text="Submit", command=submit).pack(pady=10)

        tk.Button(self.root, text="Delete Movie from Watchlist", command=delete_from_watchlist,
                  bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=5)

        tk.Button(self.root, text="Update Watchlist-Movie Association", command=update_watchlist_movie,
                  bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=5)
        def view_watchlist():
            self.clear_window()
            tk.Label(self.root, text="Watchlists", font=("Helvetica", 16), bg=self.colors["bg"],
                     fg=self.colors["fg"]).pack(pady=20)
            cursor = self.db.cursor()
            query = "SELECT w.Watchlist_id,w.Name,m.Title,m.Movie_id FROM MOVIE m JOIN WATCHLIST_MOVIE wm ON m.Movie_id=wm.Movie_id JOIN WATCHLIST w ON wm.Watchlist_id=w.Watchlist_id WHERE %s = w.User_id  "
            cursor.execute(query,self.user_id)
            movies = cursor.fetchall()

            frame1 = tk.Frame(self.root, bg=self.colors["bg"])
            frame1.pack(side="top")

            tree = ttk.Treeview(frame1, columns=("Watchlist_id","Name", "Title","Movie_id"), show="headings")
            tree.heading("Watchlist_id", text="Watchlist ID")
            tree.heading("Name", text="Watchlist")
            tree.heading("Title", text="Movie")
            tree.heading("Movie_id",text="Movie ID")

            for movie in movies:
                tree.insert("", "end", values=movie)
            tree.pack(side="top")

            tk.Button(self.root, text="Back", command=self.manage_watchlist, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=10)


        tk.Button(self.root, text="View Watchlists", command=view_watchlist, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(side="top")

        def create_watchlist():
                self.clear_window()
                tk.Label(self.root, text="Create Watchlist", font=("Helvetica", 16), bg=self.colors["bg"],
                         fg=self.colors["fg"]).pack(pady=20)
                frame = tk.Frame(self.root, bg=self.colors["bg"])
                frame.pack(pady=10)

                tk.Label(frame, text="Watchlist Name:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=0, column=0, padx=10,
                                                                                                   pady=5)
                watchlist_entry = tk.Entry(frame, bg=self.colors["entry_bg"], fg=self.colors["fg"])
                watchlist_entry.grid(row=0, column=1, padx=10, pady=5)


                def newwatchlist():
                    watchlist_name=watchlist_entry.get()
                    cursor = self.db.cursor()
                    query = "INSERT INTO WATCHLIST(Name,User_id) VALUES (%s,%s)"
                    try:
                        cursor.execute(query, (watchlist_name,self.user_id))
                        self.db.commit()
                        messagebox.showinfo("Success", "Watchlist created successfully.!")
                    except Exception as e:
                        messagebox.showerror("Error", "Watchlist could not be created.")

                tk.Button(frame, text="Add", command= newwatchlist, bg=self.colors["button"], fg=self.colors["fg"]).grid(
                    row=0, column=2, padx=10, pady=5)
                tk.Button(self.root, text="Back", command=self.manage_watchlist, bg=self.colors["button"],
                          fg=self.colors["fg"]).pack(pady=10)

        tk.Button(self.root, text="Create Watchlist", command=create_watchlist, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(side="top")

        tk.Button(self.root, text="Back", command=self.create_main_menu, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

    def explore_reviews(self):
        self.clear_window()
        tk.Label(self.root, text="Explore Reviews", font=("Helvetica", 16), bg=self.colors["bg"],
                 fg=self.colors["fg"]).pack(
            pady=20)

        cursor = self.db.cursor()
        query = "SELECT r.Review_id, m.Title, r.Rating, r.Comment FROM REVİEW r JOIN MOVIE m ON m.Movie_id = r.Movie_id"
        cursor.execute(query)
        reviews = cursor.fetchall()

        # Create Treeview to display reviews
        tree = ttk.Treeview(self.root, columns=("Review_id", "Title", "Rating", "Comment"), show="headings")
        tree.heading("Review_id", text="Review ID")
        tree.heading("Title", text="Movie")
        tree.heading("Rating", text="Rating")
        tree.heading("Comment", text="Comment")

        # Optionally hide the Review_id column for a cleaner view
        tree.column("Review_id", width=0, stretch=tk.NO)

        for review in reviews:
            tree.insert("", "end", values=review)
        tree.pack(fill=tk.BOTH, expand=True)

        def add_review():
            def submit():
                movie_id = movie_id_entry.get()
                rating = rating_entry.get()
                comment = comment_entry.get()

                cursor = self.db.cursor()
                query = "INSERT INTO REVİEW (Movie_id, Rating, Comment) VALUES (%s, %s, %s)"
                try:
                    cursor.execute(query, (movie_id, rating, comment))
                    self.db.commit()
                    messagebox.showinfo("Success", "Review added successfully.")
                    add_window.destroy()
                    self.explore_reviews()  # Refresh the review list (or relevant page)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to add review: {e}")

            add_window = tk.Toplevel(self.root)
            add_window.title("Add Review")

            tk.Label(add_window, text="Movie ID:").pack()
            movie_id_entry = tk.Entry(add_window)
            movie_id_entry.pack()

            tk.Label(add_window, text="Rating (1-5):").pack()
            rating_entry = tk.Entry(add_window)
            rating_entry.pack()

            tk.Label(add_window, text="Comment:").pack()
            comment_entry = tk.Entry(add_window)
            comment_entry.pack()

            tk.Button(add_window, text="Submit", command=submit).pack(pady=10)

        # Function to delete selected review
        def delete_review():
            selected_item = tree.selection()
            if not selected_item:
                tk.messagebox.showwarning("No selection", "Please select a review to delete.")
                return

            review_id = tree.item(selected_item)["values"][0]  # Get Review_id
            try:
                cursor = self.db.cursor()
                delete_query = "DELETE FROM REVİEW WHERE Review_id = %s"
                cursor.execute(delete_query, (review_id,))
                self.db.commit()

                # Remove from the Treeview
                tree.delete(selected_item)
                tk.messagebox.showinfo("Success", "Review deleted successfully.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {e}")

        # Function to update selected review
        def update_review():
            selected_item = tree.selection()
            if not selected_item:
                tk.messagebox.showwarning("No selection", "Please select a review to update.")
                return

            review_id = tree.item(selected_item)["values"][0]
            old_rating = tree.item(selected_item)["values"][2]
            old_comment = tree.item(selected_item)["values"][3]

            # Create a popup to input new details
            update_window = tk.Toplevel(self.root)
            update_window.title("Update Review")

            tk.Label(update_window, text="New Rating (1-10):", font=("Helvetica", 12)).pack(pady=5)
            new_rating_entry = tk.Entry(update_window, font=("Helvetica", 12))
            new_rating_entry.insert(0, old_rating)
            new_rating_entry.pack(pady=5)

            tk.Label(update_window, text="New Comment:", font=("Helvetica", 12)).pack(pady=5)
            new_comment_entry = tk.Entry(update_window, font=("Helvetica", 12))
            new_comment_entry.insert(0, old_comment)
            new_comment_entry.pack(pady=5)

            def save_update():
                new_rating = new_rating_entry.get().strip()
                new_comment = new_comment_entry.get().strip()

                if not new_rating.isdigit() or not (1 <= int(new_rating) <= 10):
                    tk.messagebox.showwarning("Invalid Input", "Rating must be a number between 1 and 10.")
                    return
                if not new_comment:
                    tk.messagebox.showwarning("Invalid Input", "Comment cannot be empty.")
                    return

                try:
                    cursor = self.db.cursor()
                    update_query = "UPDATE REVİEW SET Rating = %s, Comment = %s WHERE Review_id = %s"
                    cursor.execute(update_query, (new_rating, new_comment, review_id))
                    self.db.commit()

                    # Update the Treeview
                    tree.item(selected_item,
                              values=(review_id, tree.item(selected_item)["values"][1], new_rating, new_comment))
                    tk.messagebox.showinfo("Success", "Review updated successfully.")
                    update_window.destroy()
                except Exception as e:
                    tk.messagebox.showerror("Error", f"An error occurred: {e}")

            tk.Button(update_window, text="Save", command=save_update, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=10)
            tk.Button(update_window, text="Cancel", command=update_window.destroy, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=5)

        # Add buttons
        tk.Button(self.root, text="Add Review", command=add_review, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Delete Selected Review", command=delete_review, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Update Selected Review", command=update_review, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

    def explore_directors(self):
        self.clear_window()
        tk.Label(self.root, text="Directors", font=("Helvetica", 16), bg=self.colors["bg"], fg=self.colors["fg"]).pack(
            pady=20)

        cursor = self.db.cursor()
        query = "SELECT Director_id, Name, Nationality FROM DIRECTOR"
        cursor.execute(query)
        directors = cursor.fetchall()

        # Create Treeview to display directors
        tree = ttk.Treeview(self.root, columns=("Director_id", "Name", "Nationality"), show="headings")
        tree.heading("Director_id", text="Director ID")
        tree.heading("Name", text="Name")
        tree.heading("Nationality", text="Nationality")

        # Optionally hide the Director_id column for a cleaner view
        tree.column("Director_id", width=0, stretch=tk.NO)

        for director in directors:
            tree.insert("", "end", values=director)
        tree.pack(fill=tk.BOTH, expand=True)

        def add_director():
            def submit():
                name = name_entry.get()
                nationality = nationality_entry.get()

                cursor = self.db.cursor()
                query = "INSERT INTO DIRECTOR (Name, Nationality) VALUES (%s, %s)"
                try:
                    cursor.execute(query, (name, nationality))
                    self.db.commit()
                    messagebox.showinfo("Success", "Director added successfully.")
                    add_window.destroy()
                    self.explore_directors()  # Refresh the list of directors (or relevant page)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to add director: {e}")

            add_window = tk.Toplevel(self.root)
            add_window.title("Add Director")

            tk.Label(add_window, text="Name:").pack()
            name_entry = tk.Entry(add_window)
            name_entry.pack()

            tk.Label(add_window, text="Nationality:").pack()
            nationality_entry = tk.Entry(add_window)
            nationality_entry.pack()

            tk.Button(add_window, text="Submit", command=submit).pack(pady=10)

        # Function to delete selected director
        def delete_director():
            selected_item = tree.selection()
            if not selected_item:
                tk.messagebox.showwarning("No selection", "Please select a director to delete.")
                return

            director_id = tree.item(selected_item)["values"][0]  # Get Director_id
            try:
                cursor = self.db.cursor()
                delete_query = "DELETE FROM DIRECTOR WHERE Director_id = %s"
                cursor.execute(delete_query, (director_id,))
                self.db.commit()

                # Remove from the Treeview
                tree.delete(selected_item)
                tk.messagebox.showinfo("Success", "Director deleted successfully.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {e}")

        # Function to update selected director
        def update_director():
            selected_item = tree.selection()
            if not selected_item:
                tk.messagebox.showwarning("No selection", "Please select a director to update.")
                return

            director_id = tree.item(selected_item)["values"][0]
            old_name = tree.item(selected_item)["values"][1]
            old_nationality = tree.item(selected_item)["values"][2]

            # Create a popup to input new details
            update_window = tk.Toplevel(self.root)
            update_window.title("Update Director")

            tk.Label(update_window, text="New Name:", font=("Helvetica", 12)).pack(pady=5)
            new_name_entry = tk.Entry(update_window, font=("Helvetica", 12))
            new_name_entry.insert(0, old_name)
            new_name_entry.pack(pady=5)

            tk.Label(update_window, text="New Nationality:", font=("Helvetica", 12)).pack(pady=5)
            new_nationality_entry = tk.Entry(update_window, font=("Helvetica", 12))
            new_nationality_entry.insert(0, old_nationality)
            new_nationality_entry.pack(pady=5)

            def save_update():
                new_name = new_name_entry.get().strip()
                new_nationality = new_nationality_entry.get().strip()

                if not new_name or not new_nationality:
                    tk.messagebox.showwarning("Invalid Input", "All fields must be filled.")
                    return

                try:
                    cursor = self.db.cursor()
                    update_query = "UPDATE DIRECTOR SET Name = %s, Nationality = %s WHERE Director_id = %s"
                    cursor.execute(update_query, (new_name, new_nationality, director_id))
                    self.db.commit()

                    # Update the Treeview
                    tree.item(selected_item, values=(director_id, new_name, new_nationality))
                    tk.messagebox.showinfo("Success", "Director updated successfully.")
                    update_window.destroy()
                except Exception as e:
                    tk.messagebox.showerror("Error", f"An error occurred: {e}")

            tk.Button(update_window, text="Save", command=save_update, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=10)
            tk.Button(update_window, text="Cancel", command=update_window.destroy, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=5)

        # Add buttons
        tk.Button(self.root, text="Add New Director", command=add_director, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Delete Selected Director", command=delete_director, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Update Selected Director", command=update_director, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

    def explore_watchlists(self):
        self.clear_window()
        tk.Label(self.root, text="Watchlists", font=("Helvetica", 16), bg=self.colors["bg"], fg=self.colors["fg"]).pack(
            pady=20)

        cursor = self.db.cursor()
        query = "SELECT w.Watchlist_id, w.Name, u.Username FROM WATCHLIST w JOIN USER u ON w.User_id = u.User_id"
        cursor.execute(query)
        watchlists = cursor.fetchall()

        # Create Treeview to display watchlists
        tree = ttk.Treeview(self.root, columns=("Watchlist_id", "Name", "Username"), show="headings")
        tree.heading("Watchlist_id", text="Watchlist ID")
        tree.heading("Name", text="Watchlist Name")
        tree.heading("Username", text="Created By")



        for watchlist in watchlists:
            tree.insert("", "end", values=watchlist)
        tree.pack(fill=tk.BOTH, expand=True)

        # Function to delete selected watchlist
        def delete_watchlist():
            selected_item = tree.selection()
            if not selected_item:
                tk.messagebox.showwarning("No selection", "Please select a watchlist to delete.")
                return

            watchlist_id = tree.item(selected_item)["values"][0]  # Get Watchlist_id
            try:
                cursor = self.db.cursor()
                delete_query = "DELETE FROM WATCHLIST WHERE Watchlist_id = %s"
                cursor.execute(delete_query, (watchlist_id,))
                self.db.commit()

                # Remove from the Treeview
                tree.delete(selected_item)
                tk.messagebox.showinfo("Success", "Watchlist deleted successfully.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {e}")

        # Function to update selected watchlist
        def update_watchlist():
            selected_item = tree.selection()
            if not selected_item:
                tk.messagebox.showwarning("No selection", "Please select a watchlist to update.")
                return

            watchlist_id = tree.item(selected_item)["values"][0]
            old_name = tree.item(selected_item)["values"][1]

            # Create a popup to input the new name
            update_window = tk.Toplevel(self.root)
            update_window.title("Update Watchlist")

            tk.Label(update_window, text="New Watchlist Name:", font=("Helvetica", 12)).pack(pady=10)
            new_name_entry = tk.Entry(update_window, font=("Helvetica", 12))
            new_name_entry.insert(0, old_name)  # Prefill with the current name
            new_name_entry.pack(pady=10)

            def save_update():
                new_name = new_name_entry.get().strip()
                if not new_name:
                    tk.messagebox.showwarning("Invalid Input", "The new name cannot be empty.")
                    return

                try:
                    cursor = self.db.cursor()
                    update_query = "UPDATE WATCHLIST SET Name = %s WHERE Watchlist_id = %s"
                    cursor.execute(update_query, (new_name, watchlist_id))
                    self.db.commit()

                    # Update the Treeview
                    tree.item(selected_item, values=(watchlist_id, new_name, tree.item(selected_item)["values"][2]))
                    tk.messagebox.showinfo("Success", "Watchlist updated successfully.")
                    update_window.destroy()
                except Exception as e:
                    tk.messagebox.showerror("Error", f"An error occurred: {e}")

            tk.Button(update_window, text="Save", command=save_update, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=10)
            tk.Button(update_window, text="Cancel", command=update_window.destroy, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=10)

        # Add buttons
        tk.Button(self.root, text="Delete Selected Watchlist", command=delete_watchlist, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Update Selected Watchlist", command=update_watchlist, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

    def explore_platforms(self):
        self.clear_window()
        tk.Label(self.root, text="Platforms", font=("Helvetica", 16), bg=self.colors["bg"], fg=self.colors["fg"]).pack(
            pady=20)

        cursor = self.db.cursor()
        query = "SELECT Platform_id, Platform_name, Subscription_fee, Movie_id FROM PLATFORM"
        cursor.execute(query)
        platforms = cursor.fetchall()

        # Create Treeview to display platforms
        tree = ttk.Treeview(self.root, columns=("Platform_id", "Platform_name", "Subscription_fee", "Movie_id"),
                            show="headings")
        tree.heading("Platform_id", text="Platform ID")
        tree.heading("Platform_name", text="Platform Name")
        tree.heading("Subscription_fee", text="Subscription Fee")
        tree.heading("Movie_id", text="Movie ID")

        # Optionally hide the Platform_id column for a cleaner view
        tree.column("Platform_id", width=0, stretch=tk.NO)

        for platform in platforms:
            tree.insert("", "end", values=platform)
        tree.pack(fill=tk.BOTH, expand=True)

        # Function to add a new platform
        def add_platform():
            def submit():
                platform_name = platform_name_entry.get()
                subscription_fee = subscription_fee_entry.get()
                movie_id = movie_id_entry.get()

                cursor = self.db.cursor()
                query = "INSERT INTO PLATFORM (Platform_name, Subscription_fee, Movie_id) VALUES (%s, %s, %s)"
                try:
                    cursor.execute(query, (platform_name, subscription_fee, movie_id))
                    self.db.commit()
                    messagebox.showinfo("Success", "Platform added successfully.")
                    add_window.destroy()
                    self.explore_platforms()  # Refresh the list of platforms (or relevant page)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to add platform: {e}")

            add_window = tk.Toplevel(self.root)
            add_window.title("Add Platform")

            tk.Label(add_window, text="Platform Name:").pack()
            platform_name_entry = tk.Entry(add_window)
            platform_name_entry.pack()

            tk.Label(add_window, text="Subscription Fee:").pack()
            subscription_fee_entry = tk.Entry(add_window)
            subscription_fee_entry.pack()

            tk.Label(add_window, text="Movie ID (FK):").pack()
            movie_id_entry = tk.Entry(add_window)
            movie_id_entry.pack()

            tk.Button(add_window, text="Submit", command=submit).pack(pady=10)

        # Function to delete selected platform
        def delete_platform():
            selected_item = tree.selection()
            if not selected_item:
                tk.messagebox.showwarning("No selection", "Please select a platform to delete.")
                return

            platform_id = tree.item(selected_item)["values"][0]  # Get Platform_id
            try:
                cursor = self.db.cursor()
                delete_query = "DELETE FROM PLATFORM WHERE Platform_id = %s"
                cursor.execute(delete_query, (platform_id,))
                self.db.commit()

                # Remove from the Treeview
                tree.delete(selected_item)
                tk.messagebox.showinfo("Success", "Platform deleted successfully.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {e}")

        # Function to update selected platform
        def update_platform():
            selected_item = tree.selection()
            if not selected_item:
                tk.messagebox.showwarning("No selection", "Please select a platform to update.")
                return

            platform_id = tree.item(selected_item)["values"][0]
            old_platform_name = tree.item(selected_item)["values"][1]
            old_subscription_fee = tree.item(selected_item)["values"][2]
            old_movie_id = tree.item(selected_item)["values"][3]

            # Create a popup to input new details
            update_window = tk.Toplevel(self.root)
            update_window.title("Update Platform")

            tk.Label(update_window, text="New Platform Name:", font=("Helvetica", 12)).pack(pady=5)
            new_platform_name_entry = tk.Entry(update_window, font=("Helvetica", 12))
            new_platform_name_entry.insert(0, old_platform_name)
            new_platform_name_entry.pack(pady=5)

            tk.Label(update_window, text="New Subscription Fee:", font=("Helvetica", 12)).pack(pady=5)
            new_subscription_fee_entry = tk.Entry(update_window, font=("Helvetica", 12))
            new_subscription_fee_entry.insert(0, old_subscription_fee)
            new_subscription_fee_entry.pack(pady=5)

            tk.Label(update_window, text="New Movie ID (FK):", font=("Helvetica", 12)).pack(pady=5)
            new_movie_id_entry = tk.Entry(update_window, font=("Helvetica", 12))
            new_movie_id_entry.insert(0, old_movie_id)
            new_movie_id_entry.pack(pady=5)

            def save_update():
                new_platform_name = new_platform_name_entry.get().strip()
                new_subscription_fee = new_subscription_fee_entry.get().strip()
                new_movie_id = new_movie_id_entry.get().strip()

                if not new_platform_name or not new_subscription_fee or not new_movie_id:
                    tk.messagebox.showwarning("Invalid Input", "All fields must be filled.")
                    return

                try:
                    cursor = self.db.cursor()
                    update_query = "UPDATE PLATFORM SET Platform_name = %s, Subscription_fee = %s, Movie_id = %s WHERE Platform_id = %s"
                    cursor.execute(update_query, (new_platform_name, new_subscription_fee, new_movie_id, platform_id))
                    self.db.commit()

                    # Update the Treeview
                    tree.item(selected_item,
                              values=(platform_id, new_platform_name, new_subscription_fee, new_movie_id))
                    tk.messagebox.showinfo("Success", "Platform updated successfully.")
                    update_window.destroy()
                except Exception as e:
                    tk.messagebox.showerror("Error", f"An error occurred: {e}")

            tk.Button(update_window, text="Save", command=save_update, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=10)
            tk.Button(update_window, text="Cancel", command=update_window.destroy, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=5)

        # Add buttons
        tk.Button(self.root, text="Add New Platform", command=add_platform, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Delete Selected Platform", command=delete_platform, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Update Selected Platform", command=update_platform, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

    def explore_genres(self):
        self.clear_window()
        tk.Label(self.root, text="Genres", font=("Helvetica", 16), bg=self.colors["bg"], fg=self.colors["fg"]).pack(
            pady=20)

        cursor = self.db.cursor()
        query = "SELECT g.Genre_id, g.Name, m.Movie_id,m.Title FROM GENRE g JOIN MOVIE m ON g.Movie_id=m.Movie_id"
        cursor.execute(query)
        genres = cursor.fetchall()

        # Create Treeview to display genres
        tree = ttk.Treeview(self.root, columns=("Genre_id", "Name", "Movie_id", "Title"), show="headings")
        tree.heading("Genre_id", text="Genre ID")
        tree.heading("Name", text="Genre Name")
        tree.heading("Movie_id", text="Movie ID")
        tree.heading("Title", text="Movie")

        # Optionally hide the Genre_id column for a cleaner view
        tree.column("Genre_id", width=0, stretch=tk.NO)

        for genre in genres:
            tree.insert("", "end", values=genre)
        tree.pack(fill=tk.BOTH, expand=True)

        # Function to add a new genre
        def add_genre():
            def submit():
                genre_name = genre_name_entry.get()
                movie_id = movie_id_entry.get()

                cursor = self.db.cursor()
                query = "INSERT INTO GENRE (Name, Movie_id) VALUES (%s, %s)"
                try:
                    cursor.execute(query, (genre_name, movie_id))
                    self.db.commit()
                    messagebox.showinfo("Success", "Genre added successfully.")
                    add_window.destroy()
                    self.explore_genres()  # Refresh the list of genres (or relevant page)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to add genre: {e}")

            add_window = tk.Toplevel(self.root)
            add_window.title("Add Genre")

            tk.Label(add_window, text="Genre Name:").pack()
            genre_name_entry = tk.Entry(add_window)
            genre_name_entry.pack()

            tk.Label(add_window, text="Movie ID (FK):").pack()
            movie_id_entry = tk.Entry(add_window)
            movie_id_entry.pack()

            tk.Button(add_window, text="Submit", command=submit).pack(pady=10)

        # Function to delete selected genre
        def delete_genre():
            selected_item = tree.selection()
            if not selected_item:
                tk.messagebox.showwarning("No selection", "Please select a genre to delete.")
                return

            genre_id = tree.item(selected_item)["values"][0]  # Get Genre_id
            try:
                cursor = self.db.cursor()
                delete_query = "DELETE FROM GENRE WHERE Genre_id = %s"
                cursor.execute(delete_query, (genre_id,))
                self.db.commit()

                # Remove from the Treeview
                tree.delete(selected_item)
                tk.messagebox.showinfo("Success", "Genre deleted successfully.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {e}")

        # Function to update selected genre
        def update_genre():
            selected_item = tree.selection()
            if not selected_item:
                tk.messagebox.showwarning("No selection", "Please select a genre to update.")
                return

            genre_id = tree.item(selected_item)["values"][0]
            old_genre_name = tree.item(selected_item)["values"][1]
            old_movie_id = tree.item(selected_item)["values"][2]

            # Create a popup to input new details
            update_window = tk.Toplevel(self.root)
            update_window.title("Update Genre")

            tk.Label(update_window, text="New Genre Name:", font=("Helvetica", 12)).pack(pady=5)
            new_genre_name_entry = tk.Entry(update_window, font=("Helvetica", 12))
            new_genre_name_entry.insert(0, old_genre_name)
            new_genre_name_entry.pack(pady=5)

            tk.Label(update_window, text="New Movie ID (FK):", font=("Helvetica", 12)).pack(pady=5)
            new_movie_id_entry = tk.Entry(update_window, font=("Helvetica", 12))
            new_movie_id_entry.insert(0, old_movie_id)
            new_movie_id_entry.pack(pady=5)

            def save_update():
                new_genre_name = new_genre_name_entry.get().strip()
                new_movie_id = new_movie_id_entry.get().strip()

                if not new_genre_name or not new_movie_id:
                    tk.messagebox.showwarning("Invalid Input", "All fields must be filled.")
                    return

                try:
                    cursor = self.db.cursor()
                    update_query = "UPDATE GENRE SET Name = %s, Movie_id = %s WHERE Genre_id = %s"
                    cursor.execute(update_query, (new_genre_name, new_movie_id, genre_id))
                    self.db.commit()

                    # Update the Treeview
                    tree.item(selected_item, values=(genre_id, new_genre_name, new_movie_id))
                    tk.messagebox.showinfo("Success", "Genre updated successfully.")
                    update_window.destroy()
                except Exception as e:
                    tk.messagebox.showerror("Error", f"An error occurred: {e}")

            tk.Button(update_window, text="Save", command=save_update, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=10)
            tk.Button(update_window, text="Cancel", command=update_window.destroy, bg=self.colors["button"],
                      fg=self.colors["fg"]).pack(pady=5)

        # Add buttons
        tk.Button(self.root, text="Add New Genre", command=add_genre, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Delete Selected Genre", command=delete_genre, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Update Selected Genre Name", command=update_genre, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu, bg=self.colors["button"],
                  fg=self.colors["fg"]).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MovieWatchlistApp(root)
    root.mainloop()