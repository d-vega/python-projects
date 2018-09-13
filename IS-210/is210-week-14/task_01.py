#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Practicing with dictionary arbitrary arguments"""


import pet


class Dog(pet.Pet):
    """Organize information about your pet."""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor for Dog class.

        Args:
            has_shots(bool, optional): A truthy value to indicate if pet has
                had any shots.

            **kwargs: Arbitrary keyword arguments.
        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
        return
