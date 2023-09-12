from sklearn.metrics import confusion_matrix
import pandas as pd




def conf_mat(y_true, y_pred, labels=None, sample_weight=None, normalize=None):
	"""Compute confusion matrix to evaluate the accuracy of a classification.
	
		Parameters
		----------
		y_true : array-like of shape (n_samples,)
			Ground truth (correct) target values.

		y_pred : array-like of shape (n_samples,)
			Estimated targets as returned by a classifier.

		labels : array-like of shape (n_classes), default=None
			List of labels to index the matrix. This may be used to reorder
			or select a subset of labels.
			If ``None`` is given, those that appear at least once
			in ``y_true`` or ``y_pred`` are used in sorted order.
		
		Returns
		-------
		C :
			TN, FP, FN, TP
	"""
	tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=labels, sample_weight=sample_weight, normalize=normalize).ravel()
	
	print(f'TN: {tn}\nFP: {fp}\nFN: {fn}\nTP: {tp}')
	print()
	return tn, fp, fn, tp





