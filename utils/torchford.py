"""
Adapted from: https://github.com/a-mitani/welford/tree/main
(under the terms of the MIT license) to work with PyTorch
"""
import torch


class Welford:
    """class Welford

     Accumulator object for Welfords online / parallel variance algorithm.

    Attributes:
        count (int): The number of accumulated samples.
        mean (array(D,)): Mean of the accumulated samples.
        var_s (array(D,)): Sample variance of the accumulated samples.
        var_p (array(D,)): Population variance of the accumulated samples.
    """

    def __init__(self):
        self.__shape = None
        # current attribute values
        self.__count = 0
        self.__m = None
        self.__s = None
        # previous attribute values for rollbacking
        self.__count_old = None
        self.__m_old = None
        self.__s_old = None

    @property
    def count(self):
        return self.__count

    @property
    def mean(self):
        return self.__m

    @property
    def var_s(self):
        return self.__getvars(ddof=1)

    @property
    def var_p(self):
        return self.__getvars(ddof=0)

    def add(self, element, backup_flg=True):
        """ add

        add one data sample.

        Args:
            element (array(D, )): data sample.
            backup_flg (boolean): if True, backup previous state for rollbacking.

        """
        # Initialize if not yet.
        if self.__shape is None:
            self.__shape = element.shape
            self.__m = torch.zeros(element.shape).to(element.device)
            self.__s = torch.zeros(element.shape).to(element.device)
            self.__init_old_with_nan()
        # argument check if already initialized
        else:
            assert element.shape == self.__shape

        # backup for rollbacking
        if backup_flg:
            self.__backup_attrs()

        # Welford's algorithm
        self.__count += 1
        delta = element - self.__m
        self.__m += delta / self.__count
        self.__s += delta * (element - self.__m)

    def add_all(self, elements, backup_flg=True):
        """ add_all

        add multiple data samples.

        Args:
            elements (array(S, D)): data samples.
            backup_flg (boolean): if True, backup previous state for rollbacking.

        """
        # backup for rollbacking
        if backup_flg:
            self.__backup_attrs()

        for elem in elements:
            self.add(elem, backup_flg=False)

    def rollback(self):
        self.__count = self.__count_old
        self.__m[...] = self.__m_old[...]
        self.__s[...] = self.__s_old[...]

    def merge(self, other, backup_flg=True):
        """Merge this accumulator with another one."""
        # backup for rollbacking
        if backup_flg:
            self.__backup_attrs()

        count = self.__count + other.__count
        delta = self.__m - other.__m
        delta2 = delta * delta
        m = (self.__count * self.__m + other.__count * other.__m) / count
        s = self.__s + other.__s + delta2 * (self.__count * other.__count) / count

        self.__count = count
        self.__m = m
        self.__s = s

    def __getvars(self, ddof):
        if self.__count <= 0:
            return None
        min_count = ddof
        if self.__count <= min_count:
            return torch.full(self.__shape, torch.nan)
        else:
            return self.__s / (self.__count - ddof)

    def __backup_attrs(self):
        if self.__shape is None:
            pass
        else:
            self.__count_old = self.__count
            self.__m_old[...] = self.__m[...]
            self.__s_old[...] = self.__s[...]

    def __init_old_with_nan(self):
        self.__m_old = torch.empty(self.__shape)
        self.__m_old[...] = torch.nan
        self.__s_old = torch.empty(self.__shape)
        self.__s_old[...] = torch.nan
