# Δημιουργία παιχνιδιού: Κρεμάλα

Το πρώτο παιχνίδι που θα φτιάξουμε είναι η **Κρεμάλα**. 

## Περιγραφή

Η Κρεμάλα είναι ένα κλασικό παιχνίδι που οι περισσότεροι από εμάς έχουμε παίξει τουλάχιστον μία φορά. Στη δική μας έκδοση:

- Ο **υπολογιστής** θα επιλέγει μία λέξη από ένα σύνολο διαθέσιμων λέξεων.
- Ο **παίκτης** θα προσπαθεί να μαντέψει τη λέξη, δίνοντας ένα ένα γράμματα.
- Ο παίκτης έχει **μέγιστο περιθώριο 6 λαθών**.

## Κανόνες του παιχνιδιού

1. Ο υπολογιστής επιλέγει τυχαία μία λέξη.
2. Η λέξη εμφανίζεται με κενές θέσεις, μία για κάθε γράμμα (π.χ., `_ _ _ _ _`).
3. Ο παίκτης:
   - Μαντεύει γράμματα.
   - Αν το γράμμα υπάρχει στη λέξη, εμφανίζεται στη σωστή θέση.
   - Αν το γράμμα **δεν** υπάρχει, ο παίκτης χάνει μία από τις έξι προσπάθειες.
4. Το παιχνίδι τελειώνει όταν:
   - Ο παίκτης βρει τη λέξη (νίκη).
   - Ο παίκτης εξαντλήσει τις 6 προσπάθειες (ήττα).

## Παράδειγμα ροής παιχνιδιού

1. Ο υπολογιστής επιλέγει τη λέξη `ΜΗΛΟ`.
2. Εμφανίζεται: `_ _ _ _`
3. Ο παίκτης μαντεύει το γράμμα `Α`. 
   - **Αποτυχία**: Το γράμμα `Α` δεν υπάρχει. Απομένουν 5 προσπάθειες.
4. Ο παίκτης μαντεύει το γράμμα `Μ`. 
   - **Επιτυχία**: Ενημερώνεται η λέξη: `Μ _ _ _`.
5. Το παιχνίδι συνεχίζεται μέχρι τη νίκη ή την ήττα.

## Στοιχεία Εργασίας

> Αυτή η εργασία αποτελεί μέρος της **εργασίας Γ εξαμήνου** του μαθήματος **ΓΛΩΣΣΑ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ ΙΙΙ (Python)** στο **ΣΑΕΚ Μεσολογγίου** και δομήθηκε από τον **Σπουδαστή Κοτσόργιο Παναγιώτη**.


