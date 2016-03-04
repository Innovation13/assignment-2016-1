# Εύρεση Δικτυωμάτων σε Έναν Γράφο

Χάρη στον Edward Snowden γνωρίζουμε πλέον πολύ περισσότερα από ό,τι παλαιότερα για τον τρόπο που λειτουργούν οι μυστικές υπηρεσίες. Έτσι, [ένα από τα έγγραφα που έδωσε στη δημοσιότητα]( https://www.documentcloud.org/documents/2702948-Problem-Book-Redacted.html) αφορά στις ερευνητικές προσπάθειες της [GCHQ (Government Communications Headquarters)](https://en.wikipedia.org/wiki/Government_Communications_Headquarters), της Βρετανικής υπηρεσίας συλλογής στοιχείων.  

Ένα *k-δικτύωμα* (k-truss) σε έναν γράφο είναι ένα υποσύνολο του γράφου τέτοιο ώστε κάθε σύνδεσμος του υποσυνόλου αυτού ενισχύεται από τουλάχιστον k - 2 ζεύγη άλλων συνδέσμων τα οποία σχηματίζουν τρίγωνο με τον εν λόγω σύνδεσμο. Με άλλα λόγια, κάθε ακμή του δικτυώματος θα πρέπει να ανήκει σε k - 2 τρίγωνα με κόμβους που ανήκουν στο δικτύωμα. Για παράδειγμα, στις παρακάτω εικόνες βλέπετε τα δύο 3-δικτυώματα που έχει ένας γράφος:

<img src="truss_3_1.png" width="300"><img src="truss_3_2.png" width="300">

Ενώ στις παρακάτω εικόνες βλέπετε τα 4-δικτυώματα που έχει ένας γράφος:

<img src="truss_4_1.png" width="300"><img src="truss_4_2.png" width="300">

Και στις παρακάτω εικόνες βλέπετε τα 5-δικτυώματα που έχει ένας γράφος:

<img src="truss_5_1.png" width="250"><img src="truss_5_2.png" width="250"><img src="truss_5_3.png" width="250">

## Αλγόριθμος Επίλυσης

Πώς βρίσκουμε τα k-δικτυώματα ενός γράφου; Ένας τρόπος είναι να ακολουθήσουμε τον παρακάτω αλγόριθμο:

```
crummy_code_to_reduce_graph_to_k_truss(g, k)
    until no change do
        for each edge e = (a,b) in g:
            if (size(intersection(neighbours(a), neighbours(b)) < k - 2:
            remove e from g
    return remaining edges for each node 
```

Στον παραπάνω αλγόριθμο, η συνάρτηση `neighbours(a)` μας δίνει τους γείτονες του κόβμου `a`, η συνάρτηση `intersection(s1, s2)` βρίσκει την τομή των συνόλων `s1` και `s2`, και η συνάρτηση `size(s)` βρίσκει το μέγεθος του συνόλου `s`. Ο αλγόριθμος αυτός δεν είναι ιδιαίτερα καλός, υπάρχουν πιο αποτελεσματικοί, αλλά μας κάνει στο πλαίσιο της εργασίας.

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
python ctp.py gnp_random_graph_1.txt 3
```
με τo αρχείo [gnp_random_graph_1.txt](gnp_random_graph_1.txt), το οποίο αντιστοιχεί στον πρώτο γράφο, η έξοδος θα είναι:
```
(0, 1, 9)
(8, 10, 16)
```

* Αν ο χρήστης δώσει:
```
python ctp.py gnp_random_graph_2.txt 3
```
με τo αρχείo [gnp_random_graph_2.txt](gnp_random_graph_2.txt), το οποίο αντιστοιχεί στο δεύτερο γράφο, η έξοδος θα είναι:
```
(3, 8, 9, 18)
(7, 11, 15, 21)
```

* Αν ο χρήστης δώσει:
```
python ctp.py powerlaw_cluster_graph.txt 5
```
με τo αρχείo [powerlaw_cluster_graph.txt](powerlaw_cluster_graph.txt), το οποίο αντιστοιχεί στον τρίτο γράφο, η έξοδος θα είναι:
```
(2, 5, 8, 9, 13, 14)
(2, 5, 8, 13, 14)
(2, 8, 9, 13, 14)
```

Επαναλαμβάνουμε ότι η μορφή της εξόδου θα πρέπει να είναι ακριβώς όπως η παραπάνω για να μπορεί να αξιολογηθεί η εργασία.

Καλή Επιτυχία.
