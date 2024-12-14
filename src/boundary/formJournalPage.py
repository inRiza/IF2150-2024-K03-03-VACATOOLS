from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock  # Pastikan Clock digunakan untuk update UI
from tkinter import Tk, Toplevel, Listbox, Button as TkButton, SINGLE
from tkcalendar import Calendar  # Tambahkan impor Calendar dari tkcalendar
from ..controller.viewJournalController import ViewJournalController
from ..controller.databaseJournalController import DatabaseJournalController
from ..controller.databaseStatisticController import DatabaseStatisticController
from ..database.databaseEntity import DatabaseEntity




