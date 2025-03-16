use bevy::prelude::*;
use bevy::math::Vec2;
// mod component;
// mod constant;
use crate::core::components::*;
use crate::core::constants::*;

#[derive(Bundle)]
pub struct BoundaryBundle{
    pub boundary: Boundary,
    pub shape:Shape,
    pub position:Position,
}

impl BoundaryBundle{
    pub fn new(x:f32,y:f32,width:f32) -> Self{
        Self{
            boundary: Boundary,
            shape: Shape(Vec2::new(width,BOUNDARY_HEIGHT  )),
            position: Position(Vec2::new(x,y)),  
        }
    }
}