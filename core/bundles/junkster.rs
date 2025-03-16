use bevy::prelude::*;
use bevy::math::Vec2;
// mod component;
// mod constant;
use crate::core::components::*;
use crate::core::constants::*;

#[derive(Bundle)]
pub struct JunksterBundle{
    pub junkster: Junkster,
    pub shape:Shape,
    pub position:Position,
    pub velocity:Velocity,
}

impl JunksterBundle{
    pub fn new(x:f32,y:f32) -> Self{
        Self{
            junkster: Junkster,
            shape: Shape(Vec2::new(JUNKSTER_SIZE,JUNKSTER_SIZE )),
            position: Position(Vec2::new(0.,0.)),
            velocity: Velocity(Vec2::new(x,y))
        }
    }
}
