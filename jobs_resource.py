from flask import jsonify
from flask_restful import Resource, abort
from __all_models import *
from db_session import *
from request_parser import jobs_parser


global_init("db.db")
session = create_session()
jobs_fields = ('job', 'team_leader', 'work_size', 'collaborators',
               'is_finished', 'id')


def get_job_or_404(job_id):
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, error=f"Job {job_id} not found")
    else:
        return job


class JobsResource(Resource):
    def get(self, job_id):
        job = get_job_or_404(job_id)
        return jsonify({
            "jobs": [job.to_dict(only=jobs_fields)]
        })

    def put(self, job_id):
        args = jobs_parser.parse_args(strict=True)
        if not args:
            return jsonify({'error': 'Empty request'})
        job = get_job_or_404(job_id)
        for key, value in args.iteritems():
            setattr(job, key, value)
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, job_id):
        args = jobs_parser.parse_args(strict=True)
        if not args:
            return jsonify({'error': 'Empty request'})
        job = get_job_or_404(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        jobs = session.query(Jobs).all()
        return jsonify({
            "jobs": [job.to_dict(only=jobs_fields) for job in jobs]
        })

    def post(self):
        args = jobs_parser.parse_args(strict=True)
        if not args:
            return jsonify({'error': 'Empty request'})
        job = Jobs(**args)
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})
