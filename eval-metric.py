# Python>=3.8
# numpy~=1.22.3 

from typing import Dict

import numpy

def val_nov_metric(is_validity: numpy.ndarray, should_validity: numpy.ndarray, is_novelty: numpy.ndarray, should_novelty: numpy.ndarray) -> Dict[str, float]:
    ret = dict()

    ret_base_help = {
        "true_positive_validity": numpy.sum(numpy.where(
            numpy.all(numpy.stack([is_validity >= .5, should_validity >= .5]), axis=0),
            1, 0)),
        "true_negative_validity": numpy.sum(numpy.where(
            numpy.all(numpy.stack([is_validity < .5, should_validity < .5]), axis=0),
            1, 0)),
        "true_positive_novelty": numpy.sum(numpy.where(
            numpy.all(numpy.stack([is_novelty >= .5, should_novelty >= .5]), axis=0),
            1, 0)),
        "true_negative_novelty": numpy.sum(numpy.where(
            numpy.all(numpy.stack([is_novelty < .5, should_novelty < .5]), axis=0),
            1, 0)),
        "true_positive_valid_novel": numpy.sum(numpy.where(
            numpy.all(numpy.stack([is_validity >= .5, is_novelty >= .5,
                                   should_validity >= .5, should_novelty >= .5]), axis=0),
            1, 0)),
        "true_positive_nonvalid_novel": numpy.sum(numpy.where(
            numpy.all(numpy.stack([is_validity < .5, is_novelty >= .5,
                                   should_validity < .5, should_novelty >= .5]), axis=0),
            1, 0)),
        "true_positive_valid_nonnovel": numpy.sum(numpy.where(
            numpy.all(numpy.stack([is_validity >= .5, is_novelty < .5,
                                   should_validity >= .5, should_novelty < .5]), axis=0),
            1, 0)),
        "true_positive_nonvalid_nonnovel": numpy.sum(numpy.where(
            numpy.all(numpy.stack([is_validity < .5, is_novelty < .5,
                                   should_validity < .5, should_novelty < .5]), axis=0),
            1, 0)),
        "classified_positive_validity": numpy.sum(numpy.where(is_validity >= .5, 1, 0)),
        "classified_negative_validity": numpy.sum(numpy.where(is_validity < .5, 1, 0)),
        "classified_positive_novelty": numpy.sum(numpy.where(is_novelty >= .5, 1, 0)),
        "classified_negative_novelty": numpy.sum(numpy.where(is_novelty < .5, 1, 0)),
        "classified_positive_valid_novel": numpy.sum(numpy.where(
            numpy.all(numpy.stack([is_validity >= .5, is_novelty >= .5]), axis=0),
            1, 0)),
        "classified_positive_nonvalid_novel": numpy.sum(numpy.where(
            numpy.all(numpy.stack([is_validity < .5, is_novelty >= .5]), axis=0),
            1, 0)),
        "classified_positive_valid_nonnovel": numpy.sum(numpy.where(
            numpy.all(numpy.stack([is_validity >= .5, is_novelty < .5]), axis=0),
            1, 0)),
        "classified_positive_nonvalid_nonnovel": numpy.sum(numpy.where(
            numpy.all(numpy.stack([is_validity < .5, is_novelty < .5]), axis=0),
            1, 0)),
        "indeed_positive_validity": numpy.sum(numpy.where(should_validity >= .5, 1, 0)),
        "indeed_negative_validity": numpy.sum(numpy.where(should_validity < .5, 1, 0)),
        "indeed_positive_novelty": numpy.sum(numpy.where(should_novelty >= .5, 1, 0)),
        "indeed_negative_novelty": numpy.sum(numpy.where(should_novelty < .5, 1, 0)),
        "indeed_positive_valid_novel": numpy.sum(numpy.where(
            numpy.all(numpy.stack([should_validity >= .5, should_novelty >= .5]), axis=0),
            1, 0)),
        "indeed_positive_nonvalid_novel": numpy.sum(numpy.where(
            numpy.all(numpy.stack([should_validity < .5, should_novelty >= .5]), axis=0),
            1, 0)),
        "indeed_positive_valid_nonnovel": numpy.sum(numpy.where(
            numpy.all(numpy.stack([should_validity >= .5, should_novelty < .5]), axis=0),
            1, 0)),
        "indeed_positive_nonvalid_nonnovel": numpy.sum(numpy.where(
            numpy.all(numpy.stack([should_validity < .5, should_novelty < .5]), axis=0),
            1, 0)),
    }

    ret_help = {
        "precision_validity": ret_base_help["true_positive_validity"] /
                              max(1, ret_base_help["classified_positive_validity"]),
        "precision_novelty": ret_base_help["true_positive_novelty"] /
                             max(1, ret_base_help["classified_positive_novelty"]),
        "recall_validity": ret_base_help["true_positive_validity"] /
                           max(1, ret_base_help["indeed_positive_validity"]),
        "recall_novelty": ret_base_help["true_positive_novelty"] /
                          max(1, ret_base_help["indeed_positive_novelty"]),
        "precision_val_neg": ret_base_help["true_negative_validity"] /
                              max(1, ret_base_help["classified_negative_validity"]),
        "precision_nov_neg": ret_base_help["true_negative_novelty"] /
                             max(1, ret_base_help["classified_negative_novelty"]),
        "recall_val_neg": ret_base_help["true_negative_validity"] /
                           max(1, ret_base_help["indeed_negative_validity"]),
        "recall_nov_neg": ret_base_help["true_negative_novelty"] /
                          max(1, ret_base_help["indeed_negative_novelty"]),
        "precision_valid_novel": ret_base_help["true_positive_valid_novel"] /
                                 max(1, ret_base_help["classified_positive_valid_novel"]),
        "precision_valid_nonnovel": ret_base_help["true_positive_valid_nonnovel"] /
                                    max(1, ret_base_help["classified_positive_valid_nonnovel"]),
        "precision_nonvalid_novel": ret_base_help["true_positive_nonvalid_novel"] /
                                    max(1, ret_base_help["classified_positive_nonvalid_novel"]),
        "precision_nonvalid_nonnovel": ret_base_help["true_positive_nonvalid_nonnovel"] /
                                       max(1, ret_base_help["classified_positive_nonvalid_nonnovel"]),
        "recall_valid_novel": ret_base_help["true_positive_valid_novel"] /
                              max(1, ret_base_help["indeed_positive_valid_novel"]),
        "recall_valid_nonnovel": ret_base_help["true_positive_valid_nonnovel"] /
                                 max(1, ret_base_help["indeed_positive_valid_nonnovel"]),
        "recall_nonvalid_novel": ret_base_help["true_positive_nonvalid_novel"] /
                                 max(1, ret_base_help["indeed_positive_nonvalid_novel"]),
        "recall_nonvalid_nonnovel": ret_base_help["true_positive_nonvalid_nonnovel"] /
                                    max(1, ret_base_help["indeed_positive_nonvalid_nonnovel"])
    }

    ret.update({
        "f1_validity": 2 * ret_help["precision_validity"] * ret_help["recall_validity"] / max(1e-4, ret_help["precision_validity"] + ret_help["recall_validity"]),
        "f1_novelty": 2 * ret_help["precision_novelty"] * ret_help["recall_novelty"] / max(1e-4, ret_help["precision_novelty"] + ret_help["recall_novelty"]),
        "f1_val_neg": 2 * ret_help["precision_val_neg"] * ret_help["recall_val_neg"] / max(1e-4, ret_help["precision_val_neg"] + ret_help["recall_val_neg"]),
        "f1_nov_neg": 2 * ret_help["precision_nov_neg"] * ret_help["recall_nov_neg"] / max(1e-4, ret_help["precision_nov_neg"] + ret_help["recall_nov_neg"]),
        "f1_valid_novel": 2 * ret_help["precision_valid_novel"] * ret_help["recall_valid_novel"] / max(1e-4, ret_help["precision_valid_novel"] + ret_help["recall_valid_novel"]),
        "f1_valid_nonnovel": 2 * ret_help["precision_valid_nonnovel"] * ret_help["recall_valid_nonnovel"] / max(1e-4, ret_help["precision_valid_nonnovel"] + ret_help["recall_valid_nonnovel"]),
        "f1_nonvalid_novel": 2 * ret_help["precision_nonvalid_novel"] * ret_help["recall_nonvalid_novel"] / max(1e-4, ret_help["precision_nonvalid_novel"] + ret_help["recall_nonvalid_novel"]),
        "f1_nonvalid_nonnovel": 2 * ret_help["precision_nonvalid_nonnovel"] * ret_help["recall_nonvalid_nonnovel"] / max(1e-4, ret_help["precision_nonvalid_nonnovel"] + ret_help["recall_nonvalid_nonnovel"])
    })

    ret.update({
        "f1_val_macro": (ret["f1_validity"] + ret["f1_val_neg"])/2,
        "f1_nov_macro": (ret["f1_novelty"] + ret["f1_nov_neg"])/2,
        "f1_macro": (ret["f1_valid_novel"]+ret["f1_valid_nonnovel"]+ret["f1_nonvalid_novel"]+ret["f1_nonvalid_nonnovel"])/4
    })

    return ret
