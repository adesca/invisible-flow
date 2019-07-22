from invisible_flow.transformers import CaseInfoAllegationsTransformer


class TransformerFactory:

    @staticmethod
    def get_transformer(response_type):
        if response_type == 'Case Info':
            return CaseInfoAllegationsTransformer()
        else:
            raise Exception('Unable to handle this type of file')
