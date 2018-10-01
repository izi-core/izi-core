var gulp = require('gulp');

gulp.task('watch', function() {
    var watch = require('gulp-watch');

    gulp.watch('src/izi/static/izi/less/**/*.less', ['less']);
});
