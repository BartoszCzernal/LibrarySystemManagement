# LibrarySystemManagement
System do obsługi biblioteki miejskiej

       
    1. CRUD książki, klient(create- csv, formularz, read – wyszukiwanie, filtry)
    2. Generowanie historii danej książki
    3. Generowanie historii wypożyczeń danego klienta
    4. Dodanie wypożyczenia książki
    5. Oddanie książki
    6. Logowanie na starcie
    7. *wyslanie maila z powiadomieniem o zblizajacym sie terminie oddania
       

apps:
1.books - models: book, category, author
2.clients - models: client, address, rental, book_proposal
3.libraries - models: library, librarian(user)
