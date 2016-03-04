# Εύρεση Δικτυωμάτων σε Έναν Γράφο

Ένα *k-δικτύωμα* (k-truss) σε έναν γράφο είναι ένα υποσύνολο του γράφου τέτοιο ώστε κάθε σύνδεσμος του υποσυνόλου αυτού ενισχύεται από τουλάχιστον k - 2 ζεύγη άλλων συνδέσμων τα οποία σχηματίζουν τρίγωνο με τον εν λόγω σύνδεσμο. Για παράδειγμα, στην παρακάτω εικόνα βλέπετε τα δύο 3-δικτυώματα που έχει ένας γράφος:

<img src="truss_3_1.png" width="300"><img src="truss_3_2.png" width="300">


Αν όμως ξεκινήσετε και ανακαλύψετε στην πορεία ότι κάποιοι δρόμοι είναι αποκλεισμένοι, θα πρέπει να αναπροσαρμόσετε τη διαδρομή σας. Στην παρακάτω εικόνα θα δείτε ένα μονοπάτι που θα ακολουθήσει ένας ταξιδιώτης όταν διαπιστώνει στην πορεία ότι κάποιοι δρόμοι, τους οποίους σηματοδοτούμε με x, είναι κλειστοί.

<img src="grid_10_10_closed.png" width="600">

## Αλγόριθμος Επίλυσης

Πώς βρίσκουμε τα k-δικτυώματα ενός γράφου; Ένας τρόπος είναι να ακολουθήσουμε τον παρακάτω αλγόριθμο:

## Απαιτήσεις Προγράμματος

Κάθε φοιτητής θα εργαστεί στο προσωπικό του αποθετήριο στο GitHub. Για να αξιολογηθεί μια εργασία θα πρέπει να πληροί τις παρακάτω προϋποθέσεις:

1. Όλη η εργασία θα πρέπει να βρίσκεται σε έναν κατάλογο `assignment-2016-1` μέσα στο αποθετήριο του φοιτητή.
2. Το πρόγραμμα θα πρέπει να έχει όνομα `trusses.py`.
3. Για την υλοποίηση του γράφου θα πρέπει να χρησιμοποιήσετε λίστες γειτνίασης (adjacency lists) και όχι πίνακα γειτνίασης (adjacency matrix). Εννοείται ότι δεν επιτρέπεται η χρήση έτοιμων βιβλιοθηκών γράφων.
4. Το πρόγραμμα θα μπορεί να καλείται ως εξής:
```
python trusses.py graph_file size_of_truss
```

* Η παράμετρος `graph_file` δίνει το όνομα του αρχείου στο οποίο είναι αποθηκευμένος ο γράφος (αυτό δεν σημαίνει ότι το αρχείο ονομάζεται ντε και καλά `graph_file`, ο χρήστης μπορεί να δίνει οποιοδήποτε όνομα). Το αρχείο θα είναι της μορφής:
```
0 2
1 3 
2 4
...
```
δηλαδή αποτελείται από γραμμές που η κάθε μία περιέχει δύο αριθμούς. Αν οι δύο αριθμοί είναι οι `x`, `y` ο γράφος θα έχει ένα σύνδεσμο μεταξύ των κόμβων `x` και `y`. Ο γράφος δεν θα είναι κατευθυνόμενος, άρα θα θεωρούμε πάντα ότι θα υπάρχει και ο αντίστροφος σύνδεσμος από το `y` στο `x`. Οι κόμβοι θα είναι πάντα αριθμοί και θα είναι 0, 1, 2, ...

* Η παράμετρος `size_of_truss` είναι το μέγεθος του δικτυώματος, δηλαδή το k στο k-δικτύωμα.

### Περιγραφή Εξόδου

Η έξοδος του προγράμματος θα ιχνηλατεί τη λειτουργία του, και θα είναι *ακριβώς* όπως περιγράφεται στη συνέχεια. *Προσοχή:* αν η έξοδος δεν είναι ακριβώς σύμφωνη με την περιγραφή της, η εργασία *δεν θα μπορεί να αξιολογηθεί*.

Το πρόγραμμα θα εμφανίζει τα k-δικτυώματα του γράφου, αν υπάρχουν, με τη μορφή:
```
(0, 1, 9)
(8, 10, 16)
```
δηλαδή σε μία γραμμή θα εμφανίζεται το δικτύωμα, μέσα σε παρενθέσεις, και με τους κόμβους χωρισμένους με κόμμα και κενό μεταξύ τους. 

* Κάθε k-δικτύωμα θα εμφανίζεται μόνο μία φορά.

* Τα k-δικτυώματα θα εμφανίζονται ταξινομημένα (βλ. παρακάτω στα παραδείγματα εκτέλεσης).

### Παραδείγματα Εκτέλεσης

* Αν ο χρήστης δώσει:
```
python ctp.py gnp_random_graph.txt 3
```
με τo αρχείo [gnp_random_graph.txt](gnp_random_graph.txt), το οποίο αντιστοιχεί στην πρώτη εικόνα, η έξοδος θα είναι:
```
(0, 1, 9)
(8, 10, 16)
```

* Αν ο χρήστης δώσει:
```
python ctp.py powerlaw_cluster_graph.txt 5
```
με τo αρχείo [powerlaw_cluster_graph.txt](powerlaw_cluster_graph.txt), η έξοδος θα είναι:
```
(2, 5, 8, 9, 13, 14)
(2, 5, 8, 13, 14)
(2, 8, 9, 13, 14)
```

* Αν ο χρήστης δώσει:
```
python trusses.py powerlaw 0 99 -r -b blocked_10_10.txt
```
με τα αρχεία [grid_10_10.txt](grid_10_10.txt) και [blocked_10_10.txt](blocked_10_10.txt), τα οποία αντιστοιχούν στο παράδειγμα με το γράφο πλέγμα, αλλά με τον αλγόριθμο επανατοποθέτησης, η έξοδος θα είναι:
```
[0, 10, 0, 10, 20, 10, 0, 10, 20, 30, 20, 10, 0, 10, 20, 30, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 91, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 91, 81, 91, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 91, 81, 71, 81, 91, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 91, 81, 71, 61, 71, 81, 91, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 91, 81, 71, 61, 51, 52, 53, 54, 55, 56, 57, 58, 59, 69, 79, 89, 99]
190
```

* Αν ο χρήστης δώσει:
```
python ctp.py worst_case.txt 0 2 -b blocked_worst_case.txt
```
με τα αρχεία [worst_case.txt](worst_case.txt) και [blocked_worst_case.txt](blocked_worst_case.txt), τα οποία αντιστοιχούν στο δεύτερο παράδειγμα γράφου, η έξοδος θα είναι:
```
[0, 1, 3, 4, 5, 2]
61
```

* Αν ο χρήστης δώσει:
```
python ctp.py worst_case.txt 0 2 -r -b blocked_worst_case.txt
```
με τα αρχεία [worst_case.txt](worst_case.txt) και [blocked_worst_case.txt](blocked_worst_case.txt), τα οποία αντιστοιχούν στο δεύτερο παράδειγμα γράφου, αλλά με τον αλγόριθμο επανατοποθέτησης, η έξοδος θα είναι:
```
[0, 1, 0, 2]
14
```

* Αν ο χρήστης δώσει:
```
python ctp.py worst_case.txt 0 2
```
ή
```
python ctp.py worst_case.txt 0 2 -r
```
τότε η έξοδος θα είναι:
```
[0, 1, 2]
5
```
αφού δεν υπάρχουν κλειστοί σύνδεσμοι.

Επαναλαμβάνουμε ότι η μορφή της εξόδου θα πρέπει να είναι ακριβώς όπως η παραπάνω για να μπορεί να αξιολογηθεί η εργασία.

Καλή Επιτυχία.
