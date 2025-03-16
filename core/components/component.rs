use bevy::prelude::*;
use bevy::math::Vec2;

#[derive(Component,Debug)]
pub struct Junk;

#[derive(Component,Debug)]
pub struct Junkster;

#[derive(Component,Debug)]
pub struct Score;

#[derive(Component,Debug)]
pub struct Boundary;

#[derive(Component,Debug)]
pub struct Position(pub Vec2);

#[derive(Component,Debug)]
pub struct Velocity(pub Vec2);

#[derive(Component,Debug)]
pub struct Shape (pub Vec2);

