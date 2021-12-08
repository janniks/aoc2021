(require '[clojure.string :as str])

;; 1, 4, 7, 8 digits have unique segments
;; |  |  |  |
;; 2  4  3  7 respective number of segments

;; (defn seg_uniq? [x] (contains? #{2 3 4 7} x))

(def non_uniq? #(<= 5 % 6)) ;; == x is not 5 or 6 for ints
(def seg_uniq? #((complement non_uniq?) %))

(-> (slurp "./input/day08.txt")
    (str/split-lines)
    (->> (map #(last (str/split % #"\|\s")))
         (map #(str/split % #" ")))

    (->> (flatten)
         (map count)
         (filter seg_uniq?)
         (count)))
