-- SQL script to create tables

-- Drop existing tables
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

-- Create artists table
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);

-- Create albums table
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist_id INTEGER REFERENCES artists(id)
);
