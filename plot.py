#!/usr/bin/env python3

import math
from turtle import *

# The gravitational constant G
G = 6.67428e-11

# Assumed scale: 100 pixels = 1AU.
AU = (149.6e6 * 1000)     # 149.6 million km, in meters.
#SCALE = 250 / AU
SCALE =250/384400000
class Body(Turtle):
    """Subclass of Turtle representing a gravitationally-acting body.

    Extra attributes:
    mass : mass in kg
    ax, ay: x, y accelleration in m/s^2
    vx, vy: x, y velocities in m/s
    px, py: x, y positions in m
    """
    
    name = 'Body'
    mass = None
    ax = ay = 0.0
    vx = vy = 0.0
    px = py = 0.0
    
    
    def attraction(self, other):
        """(Body): (fx, fy)

        Returns the force exerted upon this body by the other body.
        """
        # Report an error if the other object is the same as this one.
        if self is other:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.name)

        # Compute the distance of the other body.
        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox-sx)
        dy = (oy-sy)
        d = math.sqrt(dx**2 + dy**2)

        # Report an error if the distance is zero; otherwise we'll
        # get a ZeroDivisionError exception further down.
        if d == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other.name))

        # Compute the force of attraction
        f = G * self.mass * other.mass / (d**2)

        # Compute the direction of the force.
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy

def update_info(step, bodies):
    """(int, [Body])
    
    Displays information about the status of the simulation.
    """
    print('Step #{}'.format(step))
    for body in bodies:
        s = '{:<8}  Pos.={:>6.2f} {:>6.2f} Vel.={:>10.3f} {:>10.3f}'.format(
            body.name, body.px/AU, body.py/AU, body.vx, body.vy)
        print(s)
    print()

def loop(bodies):
    """([Body])

    Never returns; loops through the simulation, updating the
    positions of all the provided bodies.
    """
    timestep = 600 # One day
    
    for body in bodies:
        body.penup()
        body.hideturtle()

    step = 1
    while True:
        update_info(step, bodies)
        step += 1

        force = {}
        for body in bodies:
            # Add up all of the forces exerted on 'body'.
            total_fx = total_fy = 0.0
            for other in bodies:
                # Don't calculate the body's attraction to itself
                if body is other:
                    continue
                fx, fy = body.attraction(other)
                total_fx += fx
                total_fy += fy

            # Record the total force exerted.
            force[body] = (total_fx, total_fy)

        # Update velocities based upon on the force.
        for body in bodies:
            fx, fy = force[body]
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep

            # Update positions
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            body.goto(body.px*SCALE, body.py*SCALE)
            body.dot(3)


def main():


    rock = Body()
    rock.name = 'rock'
    rock.mass = 10**25
    rock.px = 384400000
    rock.vy = -1200           # 29.783 km/sec
    rock.pencolor('green')

    rock2 = Body()
    rock2.name = 'rock'
    rock2.mass = 10**25
    rock2.px = -384400000
    rock2.vy = 1200          # 29.783 km/sec
    rock2.pencolor('green')

    rock3 = Body()
    rock3.name = 'rock'
    rock3.mass = 10**25
    rock3.py = 384400000
    rock3.vx = 1200           # 29.783 km/sec
    rock3.pencolor('green')

    rock3a = Body()
    rock3a.name = 'rock'
    rock3a.mass = 10**25
    rock3a.py = 384400000+100000000
    rock3a.vx = 1200+2500           # 29.783 km/sec
    rock3a.pencolor('green')

    rock4 = Body()
    rock4.name = 'rock'
    rock4.mass = 10**25
    rock4.py = -384400000
    rock4.vx = -1200           # 29.783 km/sec
    rock4.pencolor('green')

    rock4a = Body()
    rock4a.name = 'rock'
    rock4a.mass = 10**22
    rock4a.py = -384400000-100000000
    rock4a.vx = -1200-2500           # 29.783 km/sec
    rock4a.pencolor('green')

    rock40 = Body()
    rock40.name = 'rock'
    rock40.mass = 10**27
    rock40.py = 0
    rock40.vx = 0           # 29.783 km/sec
    rock40.pencolor('green')

    rock41 = Body()
    rock41.name = 'rock'
    rock41.mass = 10**22
    rock41.py = -100000000
    rock41.vx = -2500           # 29.783 km/sec
    rock41.pencolor('green')


    loop([rock, rock2, rock3, rock3a, rock4, rock4a, rock40, rock41])

if __name__ == '__main__':
    main()
