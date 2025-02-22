use bevy::prelude::*;
mod core;
use crate::core::systems::camera::*;
use crate::core::systems::window::*;
fn main() {
    App::new()
    .add_plugins(DefaultPlugins.set(create_window()))
    .add_systems(Startup, spawn_camera)
    .run();
}
