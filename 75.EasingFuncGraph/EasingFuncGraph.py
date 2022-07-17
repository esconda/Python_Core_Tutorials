#Author: Burak Dogancay
#This script shows some of the mathematical plots
import math 
class EasingBase:
    limit = (0, 1)

    def __init__(self, start: float = 0, end: float = 1, duration: float = 1):
        self.start = start
        self.end = end
        self.duration = duration

    def process(self, t: float) -> float:# float is expected return value type
        raise NotImplementedError

    def easeOp(self, alpha: float) -> float: # float is expected return value type
        t = self.limit[0] * (1 - alpha) + self.limit[1] * alpha
        t /= self.duration
        a = self.process(t)
        return self.end * a + self.start * (1 - a)

    def __call__(self, alpha: float) -> float:# float is expected return value type
        return self.easeOp(alpha)


#Quadratic easing functions

class EaseInQuad(EasingBase):
    def process(self, t: float) -> float:# float is expected return value type
        return t * t
    
class EaseOutQuad(EasingBase):
     def process(self, t: float) -> float:# float is expected return value type
        return 1 - (1 - t) * (1 - t)
    
class EaseInOutQuad(EasingBase):
    def process(self, t: float) -> float:
        if t < 0.5:
            return 2 * t * t
        return (-2 * t * t) + (4 * t) - 1

#Cubic Easing Functions

class EaseCubicIn(EasingBase):
    def func(self, t: float) -> float:
        return t * t * t

class EaseCubicOut(EasingBase):
    def process(self, t: float) -> float:# float is expected return value type
        return t * t * t

class EaseCubicInOut(EasingBase):
    def process(self, t: float) -> float:
        if t < 0.5:
            return 4 * t * t * t
        p = 2 * t - 2
        return 0.5 * p * p * p + 1
    
#Quartic easing functions

class EaseQuarticIn(EasingBase):
    def process(self, t: float) -> float:
        return t * t * t * t


class EaseQuarticOut(EasingBase):
    def process(self, t: float) -> float:
        return (t - 1) * (t - 1) * (t - 1) * (1 - t) + 1


class EaseQuarticInOut(EasingBase):
    def process(self, t: float) -> float:
        if t < 0.5:
            return 8 * t * t * t * t
        p = t - 1
        return -8 * p * p * p * p + 1
    
#Quintic easing functions
class EaseQuinticIn(EasingBase):
    def process(self, t: float) -> float:
        return t * t * t * t * t


class EaseQuinticOut(EasingBase):
    def process(self, t: float) -> float:
        return (t - 1) * (t - 1) * (t - 1) * (t - 1) * (t - 1) + 1


class EaseQuinticInOut(EasingBase):
    def process(self, t: float) -> float:
        if t < 0.5:
            return 16 * t * t * t * t * t
        p = (2 * t) - 2
        return 0.5 * p * p * p * p * p + 1


#Sine easing functions
class EaseSineIn(EasingBase):
    def process(self, t: float) -> float:
        return math.sin((t - 1) * math.pi / 2) + 1


class EaseSineOut(EasingBase):
    def process(self, t: float) -> float:
        return math.sin(t * math.pi / 2)


class EaseSineInOut(EasingBase):
    def process(self, t: float) -> float:
        return 0.5 * (1 - math.cos(t * math.pi))

