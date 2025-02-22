use bevy::prelude::*;
use bevy::math::Vec2;

#[derive(Component)]
pub struct Junk;

#[derive(Component)]
pub struct Junkster;

#[derive(Component)]
pub struct Score;

#[derive(Component)]
pub struct Boundary;

#[derive(Component)]
pub struct Position(pub Vec2);

#[derive(Component)]
pub struct Velocity(pub Vec2);

#[derive(Component)]
pub struct Shape (pub Vec2);

