from .forms import SubCateFormInsert


def Create_Prefix_FromInsert(mainNo,topic,username):
    prefix = 'form' + str(topic)
    SubNo = str(mainNo) + str(topic)
    form = SubCateFormInsert(prefix=prefix)
    form.setValueSubNo(SubNo)
    form.setValueUsername(username)
    return (prefix,form)