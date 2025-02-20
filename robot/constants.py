import math

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Robot Container Input System
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DRIVER_CONTROLLER_PORT = 0

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Motor and Motor controller IDs
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
FRONT_RIGHT_DRIVE_ID = 4
FRONT_RIGHT_TURN_ID = 44

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Swerve turningPIDController variables
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
MODULE_MAX_ANGULAR_VELOCITY = math.tau
MODULE_MAX_ANGULAR_ACCELERATION = 2*math.tau
SWERVE_TURN_GEAR_RATIO = 2.099982500145832 / 42

# Front Left
TURN_FRONT_LEFT_P = 13
TURN_FRONT_LEFT_I = 0
TURN_FRONT_LEFT_D = .3

# Front Right
TURN_FRONT_RIGHT_P = TURN_FRONT_LEFT_P + 0
TURN_FRONT_RIGHT_I = TURN_FRONT_LEFT_I + 0
TURN_FRONT_RIGHT_D = TURN_FRONT_LEFT_D + 0

