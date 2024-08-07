from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from CollideObjectBase import *

class Universe(InverseSphereCollideObject):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 0.9)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

class Planet(SphereCollideObject):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        super(Planet, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1.1)
        
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

class SpaceStation(CapsuleCollidableObject):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        super(SpaceStation, self).__init__(loader, modelPath, parentNode, nodeName, 1, -1, 5, 1, -1, -5, 10)
        
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

class Drone(SphereCollideObject):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        super(Drone, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 5.0)
        
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

    droneCount = 0
    ogDC = 0

class Boss(SphereCollideObject):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        super(Boss, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 5.0)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)
        self.modelNode.setColorScale(1.0, 0.0, 0.0, 1.0)

    summonCount = 0
    HP = 3

class Missile(SphereCollideObject):
    fireModels = {}
    cNodes = {}
    collisionSolids = {}
    Intervals = {}
    missileCount = 0

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float = 1.0):
        super(Missile, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 3.0)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setPos(posVec)

        Missile.missileCount += 1
        Missile.fireModels[nodeName] = self.modelNode
        Missile.cNodes[nodeName] = self.collisionNode
        Missile.collisionSolids[nodeName] = self.collisionNode.node().getSolid(0)
        Missile.cNodes[nodeName].show()

        print("Fire torpedo #" + str(Missile.missileCount))