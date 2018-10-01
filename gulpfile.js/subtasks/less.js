var gulp = require('gulp'),
    less = require('gulp-less'),
    sourcemaps = require('gulp-sourcemaps'),
    pump = require('pump'),
    less_task = function(cb) {
        pump([
            gulp.src('src/izi/static/izi/less/*.less'),
            sourcemaps.init(),
            less({includePaths: [
                    'src/izi/static/less/',
                    ],
                    outputStyle: null,
                }),
            sourcemaps.write('/'),
            gulp.dest('src/izi/static/izi/css/')
            ],
            cb
        );
    };

gulp.task('less', less_task);
