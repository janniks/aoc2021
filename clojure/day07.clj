(require '[clojure.string :as string])

(def input (-> (slurp "./input/day07.txt")
               (string/trim)
               (string/split #",")
               (->> (map read-string))))

input

;; that's enough clojure for today
