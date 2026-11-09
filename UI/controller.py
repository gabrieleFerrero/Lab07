import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        """Popola i dropdown di biblioteche e generi con l'opzione iniziale 'Nessun filtro'."""
        # --- Popola Dropdown Biblioteche ---
        self._view.dd_biblioteca.options.clear()
        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="NONE", text="Nessun filtro"))

        biblioteche = self._model.get_biblioteche()
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(b.id), text=b.nome))

        # --- Popola Dropdown Generi ---
        self._view.dd_genere.options.clear()
        self._view.dd_genere.options.append(ft.dropdown.Option(key="NONE", text="Nessun filtro"))

        generi = self._model.get_generi()
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(key=g, text=g))
    # TODO

    # CALLBACKS DROPDOWN
    def on_select_biblioteca(self, e):
        """Gestisce la selezione della biblioteca dal dropdown."""
        valore = self._view.dd_biblioteca.value
        if valore == "NONE" or valore is None:
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = int(valore)

    def on_select_genere(self, e):
        """Gestisce la selezione del genere dal dropdown."""
        valore = self._view.dd_genere.value
        if valore == "NONE" or valore is None:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore
    # TODO

    # AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
        """Legge i dati filtrati dal Modello e popola la ListView o mostra un alert se vuota."""
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        self._view.lst_libri.controls.clear()

        if not libri:
            self._view.show_alert("Nessun libro trovato con i criteri di filtraggio selezionati.")
        else:
            for libro in libri:
                self._view.lst_libri.controls.append(ft.Text(str(libro)))

        self._view.update()
    # TODO
