######
#TODO: === Design Pattern Behavior - Work Algorithms -: Command (Comando) ===
#?: Command es un patrón de diseño de comportamiento que convierte una solicitud en un objeto independiente que contiene toda la información sobre la solicitud. Esta transformación te permite parametrizar los métodos con diferentes solicitudes, retrasar o poner en cola la ejecución de una solicitud y soportar operaciones que no se pueden realizar.
#############
from abc import ABC, abstractmethod


#? == Comando (Command) ==
class Button(ABC): 
  @abstractmethod
  def execute(self):
    pass


#? === Receptor (Receiver) ===
class Light: 
  def turn_on(self) -> str:
    light_on = f"Turn On!"
    print(light_on)

  def turn_off(self) -> str: 
    light_off = f"Turn Off!!"
    print(light_off)


class ApplyLightLed:
  def light_led(self) -> str: 
    apply_led = f"New Light Led!"
    print(apply_led)


#? ==== Comandos concretos (Concrete Commands) ==== 
class LightOnBtn(Button): 
  def __init__(self, light): 
    self.light = light

  def execute(self):
    return self.light.turn_on()
  

class LightOffBtn(Button):
  def __init__(self, light): 
    self.light = light

  def execute(self):
    return self.light.turn_off()
  

class ApplyLightLedOn(Button):
  def __init__(self, light):
    self.light = light
  
  def execute(self): 
    return self.light.light_led()

#? ===== === Invocador (Invoker) === =====
class InvokerPlus: 
  def __init__(self): 
    self.button = None

  def set_btn(self, button): 
     self.button = button

  def press_btn(self): 
    new_btn = self.button.execute()
    return new_btn

  

#! ======= > Execute: Main < ========
if __name__ == "__main__":
  #? > Client <
  # Configurar objetos
  lights = Light()
  apply_led_light = ApplyLightLed()

  btn_on = LightOnBtn(lights)
  btn_off = LightOffBtn(lights)
  btn_click_off = ApplyLightLedOn(apply_led_light)
  #btn_off.execute()

  # Configurar el control remoto
  remote = InvokerPlus()
  remote_off = InvokerPlus()
  remote_apply = InvokerPlus()
  
  # Asignar comandos y ejecutarlos
  remote.set_btn(btn_on)
  remote.press_btn()

  remote_off.set_btn(btn_off)
  remote_off.press_btn()

  remote_apply.set_btn(btn_click_off)
  remote_apply.press_btn()