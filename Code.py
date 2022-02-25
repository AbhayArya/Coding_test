import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


class XmlProcessor:
    def read_xml_file(self, file_path):
        """
        in:
        file_path: path of xml file for reading.

        out:
        return the parent object of xml.

        """
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            return root
        except Exception as ex:
            print("No xml file at given file path location: {}".format(ex))

    def write_xml_file(self, root, file_path):
        """
        in:
        root: parent node/object of xml.
        file_path: path of xml file for reading.

        out:
        write the complete to xml file at given file_path

        """
        try:
            with open(file_path, 'wb') as f:
                f.write(ET.tostring(root))
            f.close()
        except Exception as ex:
            print("Error file writing to xml file. {}".format(ex))

    def add_employee(self, root, attributes_list, value_list, file_path):
        """
        in:
        root: parent node/object of xml.
        attributes_list: List of attribute for new employee
        value_list: List of value corresponding to each attributes
        file_path: save the xml to given file_path having new employee details.

        out:
        added new employee to existing xml file with given employee details.

        """
        try:
            attributes_obj = []
            emp_list = root.findall('employee')
            new_emp = Element("employee")

            for attribute in attributes_list:
                attr = ET.SubElement(new_emp, attribute)
                attributes_obj.append(attr)

            for i in range(len(attributes_obj)):
                attributes_obj[i].text = value_list[i]

            root.append(new_emp)

            self.write_xml_file(root, file_path)
        except Exception as ex:
            print(ex)

    def add_sub_attribute_for_employee(self, root, attribute, sub_attributes_list, value_list, file_path, **kwargs):
        """
        in:
        root: parent node/object of xml.
        attribute: attribute name for employee i.e, address, Qualification
        attributes_list: List of attribute for new employee i.e, for address (doorNo, street, State)
        value_list: List of value corresponding to each attributes i.e, for address (10, 'Edapally', 'Kerala')
        file_path: save the xml to given file_path having new employee details.
        kwargs: keyword arguments to decide for which employee new attributes is to be added.
        out:
        add new attributes and it's sub attributes for given employee to existing xml file.

        """
        try:
            sub_attributes_elements = []
            for key, value in kwargs.items():
                emp_list = root.findall('employee')
                for emp in emp_list:
                    for node in emp.findall(key):
                        if node.text.lower() == value.lower():

                            new_attr = ET.SubElement(emp, attribute)

                            for attribute in sub_attributes_list:
                                sub_attr = ET.SubElement(new_attr, attribute)
                                sub_attributes_elements.append(sub_attr)

                            for i in range(len(sub_attributes_elements)):
                                sub_attributes_elements[i].text = value_list[i]

            self.write_xml_file(root, file_path)
        except Exception as ex:
            print(ex)

    def delete_employee(self, root, file_path, **kwargs):
        """
        in:
        root: parent node/object of xml.
        file_path: save the modified xml to given file_path.
        **kwargs: can pass multiple keywords arguments e.g, name='Mohan', age='25'.

        out:
        Based on argument provide, if details are present then that employee details will get removed from xml file.

        """
        is_available = False
        try:
            for key, value in kwargs.items():
                emp_list = root.findall('employee')
                for emp in emp_list:
                    for node in emp.findall(key):
                        if node.text.lower() == value.lower():
                            is_available = True
                            root.remove(emp)

            if not is_available:
                print("No employee available with given details")

            self.write_xml_file(root, file_path)
        except Exception as ex:
            print(ex)


if __name__ == '__main__':

    # problem 1

    xml_processor1 = XmlProcessor()
    filepath = r'C:\Users\q1036048\Desktop\test_peer.xml'
    parent_obj = xml_processor1.read_xml_file(filepath)

    #
    #
    # # add new employee
    # attributes_list = ['name', 'age', 'designation']
    # value_list = ['Ram', '30', 'Software Engineer']
    # xml_processor1.add_employee(parent_obj, attributes_list, value_list, filepath)
    #
    #
    # # delete employee
    # xml_processor1.delete_employee(parent_obj, filepath, name='Ram')



    # problem 2

    # xml_processor2 = XmlProcessor()
    # filepath = r'C:\Users\q1036048\Desktop\test_peer.xml'
    # parent_obj = xml_processor2.read_xml_file(filepath)
    #
    #
    # # add attribute to existing employee
    # attribute = 'address'
    # sub_attributes_list = ['doorNo', 'street', 'town', 'state']
    # value_list = ['10', 'Edapally', 'Ernakulam', 'Kerala']
    # xml_processor2.add_sub_attribute_for_employee(parent_obj, attribute, sub_attributes_list, value_list,
    #                                               filepath, name='Ram')

    # # to add new node
    # attribute = 'Qualifications'
    # sub_attributes_list = ['UG', 'PG', 'certifications']
    # value_list = ['CUSAT', 'CUSAY', 'CKAD']
    # xml_processor2.add_sub_attribute_for_employee(parent_obj, attribute, sub_attributes_list, value_list,
    #                                               filepath, name='Ram')
