;; if a path starts with "//", we replace it with other path
;; macro code when cd is frequently used

(defun ecd (dir) "cd extended" (interactive)
       (cond
	((string-prefix-p "//" dir) (cd (concat "C:/" (seq-subseq dir 2))))
	((string-prefix-p "//" dir) (cd (concat "C:/" (seq-subseq dir 2))))
	((string-prefix-p "//" dir) (cd (concat "C:/" (seq-subseq dir 2))))
)
