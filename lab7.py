import numpy as np
import math
import pathlib
import sys

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from extras.axes import AxesHelper
from extras.grid import GridHelper
from extras.movement_rig import MovementRig
from core_ext.texture import Texture
from geometry.cylinder import CylinderGeometry
from geometry.handle import HandleGeometry
from geometry.sphere import SphereGeometry
from material.texture import TextureMaterial
from geometry.bow import BowMesh
from extras.movement_player import MovementPlayer
from geometry.arrow import ArrowMesh
from geometry.target import TargetMesh
from geometry.tripe import TripeMesh
from extras.movement_arrow import MovementArrow
from geometry.rectangle import RectangleGeometry
from material.sprite import SpriteMaterial
from geometry.game_over import GameOver
from geometry.main_page import MainPageMesh
from geometry.instructions import InstructionsMesh
from geometry.winning import Winning
from extras.movement_camera import MovementCamera


class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add camera movement: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.cameraRig = MovementCamera()
        self.rig = MovementRig()
        self.cameraRig.add(self.camera)
        self.rig.add(self.cameraRig)
        # self.camera.set_position([0,0,5])
        self.bow = BowMesh()
        self.bow.scale(0.5)
        self.arrow = ArrowMesh()
        self.bow.set_position([-0.3,0,-0.3])
        self.arrow.set_position([-0.175,0.3,0])
        self.arrow.rotate_x(-math.pi/2, local=False)


        geometry = RectangleGeometry(width = 1, height = 0.3)
        tile_set = Texture("images/energy_bar.png")
        sprite_material = SpriteMaterial(tile_set, {
            "billboard" : 1, 
            "tileCount" : [1, 4],
            "tileNumber" : 0 
        })

        geometry1 = RectangleGeometry(width = 1, height = 0.25)
        tile_set1 = Texture("images/arrow_number1.png")
        sprite_material1 = SpriteMaterial(tile_set1, {
            "billboard" : 1, 
            "tileCount" : [1, 4],
            "tileNumber" : 0 
        })

        self.mainPage = MainPageMesh()
        self.mainPage.set_position([10, 0, 100])

        self.instructions = InstructionsMesh()
        self.instructions.set_position([7.5, 0, 100])

        self.gameOver = GameOver()
        self.gameOver.set_position([5, 0, 100])

        self.winning = Winning()
        self.winning.set_position([2.5, 0, 100])

        self.sprite = Mesh(geometry, sprite_material)
        self.sprite.set_position([1,-1,-2])
        self.sprite1 = Mesh(geometry1, sprite_material1)
        self.sprite1.set_position([1,-0.75,-2])
        self.rig.add(self.bow)
        self.rig.add(self.arrow)
        self.rig.add(self.sprite)
        self.rig.add(self.sprite1)
        self.rig.set_position([0, 0, 20])
        self.scene.add(self.rig)

        self.arrows=[]
        self.arrows.append(ArrowMesh())
        self.arrows.append(ArrowMesh())
        self.arrows.append(ArrowMesh())
        self.arrows[0].set_position([-2, 0, 0])
        self.arrows[1].set_position([-2, 2, 0])
        self.arrows[2].set_position([2, 0, 0])

        self.target = TargetMesh()
        self.target.translate(-2,0,0)
        self.target.rotate_x(math.pi/2)

        self.tripe = TripeMesh()
        self.tripe.translate(2,2,0)

        # NIVEL 1
        self.sky_geometry = SphereGeometry(radius=25)
        self.sky_material = TextureMaterial(texture=Texture(file_name="images/sky1.jpg"), property_dict={"doubleSide": True})
        self.sky = Mesh(self.sky_geometry, self.sky_material)
        self.scene.add(self.sky)
        self.grass_geometry = RectangleGeometry(width=50, height=50)
        self.grass_material = TextureMaterial(
            texture=Texture(file_name="images/stone.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        self.grass = Mesh(self.grass_geometry, self.grass_material)
        self.grass.rotate_x(-math.pi/2)
        self.grass.translate(0,0,-1.5)
        self.scene.add(self.grass)
        #=================================================

        #NIVEL 2
        nether_sky_geometry = SphereGeometry(radius=25)
        nether_sky_material = TextureMaterial(texture=Texture(file_name="images/red_sky.jpg"), property_dict={"doubleSide": True})
        nether_sky = Mesh(nether_sky_geometry, nether_sky_material)
        nether_sky.translate(51,0,0)
        self.scene.add(nether_sky)
        nether_geometry = RectangleGeometry(width=50, height=50)
        nether_material = TextureMaterial(
            texture=Texture(file_name="images/nether.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        nether = Mesh(nether_geometry, nether_material)
        nether.rotate_x(-math.pi/2)
        nether.translate(51,0,-1.5)
        self.scene.add(nether) 
        #=================================================

        #NIVEL 3
        end_sky_geometry = SphereGeometry(radius=25)
        end_sky_material = TextureMaterial(texture=Texture(file_name="images/end_sky.jpg"), property_dict={"doubleSide": True})
        end_sky = Mesh(end_sky_geometry, end_sky_material)
        end_sky.translate(-51,0,0)
        self.scene.add(end_sky)
        end_geometry = RectangleGeometry(width=50, height=50)
        end_material = TextureMaterial(
            texture=Texture(file_name="images/end.jpg"),
            property_dict={"repeatUV": [40, 40]}
        )
        end = Mesh(end_geometry, end_material)
        end.rotate_x(-math.pi/2)
        end.translate(-51,0,-1.5)
        self.scene.add(end)
        #=================================================

        self.scene.add(self.arrows[0])
        self.scene.add(self.arrows[1])
        self.scene.add(self.arrows[2])
        self.scene.add(self.target)
        self.scene.add(self.tripe)
        self.scene.add(self.mainPage)
        self.scene.add(self.instructions)
        self.scene.add(self.gameOver)
        self.scene.add(self.winning)

        self.lives = 3
        self.angle = 0
        self.shooting = False
        self.level = 1

        self.tiro = -1
        self.collision = False



    def update(self):
        self.cameraRig.update(self.input, self.delta_time*2)
        self.renderer.render(self.scene, self.camera)
        if self.cameraRig.isGame == True:
            self.rig.update(self.input, self.delta_time*2)
            if self.lives == 0 and self.collision == True:
                self.rig._look_attachment.set_local_matrix(self.rig.getInitalMatrix())
                self.cameraRig.set_position([5,0,80.75])
                self.cameraRig.isGame == False
                self.cameraRig.setPlay(False)
                self.lives = 3
                self.tiro = -1
                self.level = self.level+1
            if self.rig.isShooting() == True and self.shooting == False:
                print("ola")
            if self.rig.isShooting() == True and self.shooting == True:
                if self.rig.getPower() < 5:
                    self.angle = self.angle + 1/self.rig.getPower()*0.1
                elif self.rig.getPower() < 30:
                    self.angle = self.angle + 1/self.rig.getPower()*0.5
                else:
                    self.angle = self.angle + 1/self.rig.getPower()*1
                self.arrows[self.tiro].translate(0,self.rig.getPower()*0.01,math.cos(self.angle)-1)

            else:
                self.shooting = False
                self.angle = 0
                self.rig._look_attachment.children_list[2].set_position([-0.175,0,0])
                tileNumber = math.floor(self.rig.getPower() / 30)
                self.sprite.material.uniform_dict["tileNumber"].data = tileNumber
                tileNumber1 = self.lives
                self.sprite1.material.uniform_dict["tileNumber"].data = tileNumber1
                self.rig.update(self.input, self.delta_time)
        else:
            self.rig._look_attachment.set_local_matrix(self.rig.getInitalMatrix())

        # print(self.arrows[self.tiro].global_position[2])
        if self.arrows[self.tiro].global_position[1] < self.grass.global_position[1]+0.175:
            self.rig.setShooting(False)
            self.collision = True

        


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
