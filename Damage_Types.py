class Mundane_Damage():
    def __init__(self,damage,power,penetration):
        pass
    #mundane damage types
    def blunt_damage(self,damage,power,penetration):
        pass

    def slashing_damage(self,damage,power,penetration):
        pass

    def poison_dmg(self,damage,power,penetration):
        pass

    def piercing_damage(self,damage,power,penetration):
        pass

    def un_armed_damage(self,damage,power,penetration):
        pass


class Magic():
#magic damage types
    def __init__(self,magic_damage,magic_power,magic_penetration):
        pass

    def light_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    def dark_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    def fire_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    def water_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    def earth_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    def air_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass


class Higher_Magic(Magic):
#hybrid damage types
    def __init__(self,magic_damage,magic_power,magic_penetration):
        pass

    #higher light magic
    def blessed_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    #higher dark magic
    def cursed_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    #water+fire higher magics
    def ice_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    #air+earth higher magics
    def lightning_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    #water+earth higher magics
    def nature_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    #water+air higher magics
    def corrosive_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    #air+fire higher magics
    def lifefire_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    #air+earth higher magics
    def magma_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass

    #light+dark higher magics
    def grey_magic_damage(self,magic_damage,magic_power,magic_penetration):
        pass