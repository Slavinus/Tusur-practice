class Hero():
    def __init__(self, name):
        self._name = name
        self._level = 1
        self._xp = 0
        self._hp = self.max_hp

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def xp(self):
        return self._xp

    @property
    def max_hp(self):
        return 100 + 20 * (self._level - 1)

    @property
    def hp(self):
        return self._hp

    @property
    def is_alive(self):
        return self._hp > 0

    def gain_xp(self, points):
        if not self.is_alive:
            raise ValueError("Сдох")
        if points <= 0:
            raise ValueError("а поч опыта нет???")
        self._xp += points
        leveled_up = False
        while self._xp >= 100 * self._level:
            self._xp -= 100 * self._level
            self._level += 1
            leveled_up = True
        if leveled_up:
            self._hp = self.max_hp

    def take_damage(self, amount):
        if amount <= 0:
            raise ValueError ("Слабенько как то")
        self._hp = max(0,self._hp - amount)

    def heal(self, amount):
        if not self.is_alive:
            raise ValueError ("что ты там хилить собрался?")
        if amount <= 0:
            raise ValueError ("чё?")
        self._hp = min(self.max_hp, self._hp + amount)

    def attack(self, other):
        if not isinstance(other, Hero):
            raise TypeError("ты мазахист?")
        if not self.is_alive:
            raise ValueError ("Сдох")
        if other is self:
            raise ValueError ("не надо")
        if not other.is_alive:
            raise ValueError("Он умер уже, отстань")
        other.take_damage(10*self._level)
        if not other.is_alive:
            self.gain_xp(50 * other.level)

    def __repr__(self):
        return (f"Hero({self._name!r}, level={self._level},"
                f" xp={self._xp}, hp={self.hp}/{self.max_hp})")